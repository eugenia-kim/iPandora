import logging

from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import BasicAuthentication

from app.api.csrf import CsrfExemptSessionAuthentication
from app.api.models.Given import Given, GivenSerializer
from app.api.models.Types import Type, TypeSerializer
from app.api.utils import Z3Exception

logger = logging.getLogger(__name__)

@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
class GivenViewSet(viewsets.ModelViewSet):

        #API endpoint that allows users to be viewed or edited.
    queryset = Given.objects.all()
    serializer_class = GivenSerializer

    @csrf_exempt
    def create(self, request):
        serializer = GivenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            type_query = Type.objects.filter(proofId=request.data['proofId'])
            types = [t['text'] for t in TypeSerializer(type_query, many=True).data]
            type_valid, param_map, predicate_map = Type.get_maps(types)
            if not type_valid:
                raise Z3Exception('Type Declarations Error', 'text', status.HTTP_400_BAD_REQUEST)
            try:
                step_valid = Given.z3_valid(serializer.validated_data['text'], param_map, predicate_map)
            except Exception as err:
                raise Z3Exception(err, 'text', status.HTTP_400_BAD_REQUEST)
            if not step_valid:
                raise Z3Exception('Syntax Error', 'text', status.HTTP_400_BAD_REQUEST)
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        query = Given.objects.filter(proofId=request.query_params['proofId'])
        serializer = GivenSerializer(query, many=True)
        return Response(serializer.data)
