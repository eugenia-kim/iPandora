import logging

from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import BasicAuthentication

from app.api.csrf import CsrfExemptSessionAuthentication
from app.api.models.Justification import Justification, JustificationSerializer
from app.api.models.Step import Step, StepSerializer
from app.api.models.Given import Given, GivenSerializer
from app.api.models.Types import Type, TypeSerializer
from app.api.utils import Z3Exception

logger = logging.getLogger(__name__)

@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
class StepViewSet(viewsets.ModelViewSet):

        #API endpoint that allows users to be viewed or edited.
    queryset = Step.objects.all()
    serializer_class = StepSerializer

    @csrf_exempt
    def create(self, request):
        serializer = StepSerializer(data=request.data)
        logger.error(request.data)
        if serializer.is_valid(raise_exception=True):
            logger.error(serializer.validated_data)
            if not serializer.validated_data['isZ3Formula']:
                # "Take arbitrary x1"
                serializer.validated_data['forall'] = True
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            # building types
            type_query = Type.objects.filter(proofId=request.data['proofId'])
            types = [t['text'] for t in TypeSerializer(type_query, many=True).data]
            type_valid, param_map, predicate_map = Type.get_maps(types)
            if not type_valid:
                raise Z3Exception('Type Declarations Error', 'text', status.HTTP_400_BAD_REQUEST)
            print("BUILDING STEP NOW")
            # building step
            quantifier = dict()
            try:
                step_valid, step_builder = Step.z3_valid(serializer.validated_data['text'], param_map, predicate_map, quantifier)
                print(step_valid)
            except Exception as err:
                raise Z3Exception(err, 'text', status.HTTP_400_BAD_REQUEST)

            if not step_valid:
                raise Z3Exception('Syntax Error', 'text', status.HTTP_400_BAD_REQUEST)
            elif serializer.validated_data['isFirstStepInBox'] or serializer.validated_data['skipProof']:
                # Assumption
                serializer.validated_data['exist'] = quantifier.get('exist')
                serializer.validated_data['forall'] = quantifier.get('forall')
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            #checking the justifications
            proofId = request.data.get('proofId')
            given_ids = [g for g in request.data.getlist('givenJust')]
            step_ids = [s for s in request.data.getlist('stepJust')]

            # building proof
            givenJust = [Given.objects.get(id=g, proofId=proofId).text for g in given_ids]
            stepJust = [Step.objects.get(id=s, proofId=proofId).text for s in step_ids]


            print("GETTING THE JUSTIFICATIONS")
            logger.error(givenJust)
            logger.error(stepJust)

            try:
                proof_valid = Step.proof_valid(step_builder, serializer.validated_data['text'], givenJust, stepJust)
            except Exception as err:
                raise Z3Exception(err, 'text', status.HTTP_400_BAD_REQUEST)

            if proof_valid:
                serializer.validated_data['exist'] = quantifier.get('exist')
                serializer.validated_data['forall'] = quantifier.get('forall')
                instance = serializer.save()

                # building Justification Model
                for justification in step_ids:
                    self.__createJustificationModel(instance.id, justification)

                logger.error(serializer.data)
                return Response(serializer.data, status=status.HTTP_200_OK)

            #print(proof_valid)
            print(Step.proof_sat(step_builder, serializer.validated_data['text'], givenJust, stepJust))

            raise Z3Exception('Proof is not Valid', 'text', status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        query = Step.objects.filter(proofId=request.query_params['proofId'])
        serializer = StepSerializer(query, many=True)
        responseData = list(map(lambda data: self.__addStepJustInResponse(data, self.__getJustificationIdList(data['id'])), serializer.data))
        return Response(responseData)

    def __createJustificationModel(self, stepId, justificationId):
        print("CREATEJUSTIFICATIONMODEL")
        justification = dict()
        justification['step'] = stepId
        justification['justification'] = justificationId
        serializer = JustificationSerializer(data=justification)
        if serializer.is_valid(raise_exception=True):
            print("IN IF NOW")
            serializer.save()

    def __getJustificationIdList(self, stepId):
        return map(lambda obj: obj.justification.id, Justification.objects.filter(step=stepId))

    def __addStepJustInResponse(self, data, stepJust):
        responseData = data.copy()
        responseData['stepJust'] = stepJust
        return responseData

