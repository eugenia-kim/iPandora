import logging

from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from app.api.models.Proof import ProofSerializer
from app.api.models.Types import Type, TypeSerializer
from app.api.models.Given import Given, GivenSerializer

logger = logging.getLogger(__name__)

@api_view(['GET'])
def init_dec(req):
    return JsonResponse({'dec': True})


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

@api_view(['POST'])
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def begin_proof(request):
    serializer = ProofSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        return redirect('/' + str(instance.id))
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    @csrf_exempt
    def create(self, request):
        serializer = TypeSerializer(data=request.data)
        prev_query = Type.objects.filter(proofId=request.data['proofId'])
        types = [t['text'] for t in TypeSerializer(prev_query, many=True).data]
        if serializer.is_valid():
            serializer.save()
            types.append(serializer.data['text'])
            type_valid = Type.is_valid(types)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Type.objects.filter(proofId=request.query_params['proofId'])
        serializer = TypeSerializer(queryset, many=True)
        return Response(serializer.data)

@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
class GivenViewSet(viewsets.ModelViewSet):
        #API endpoint that allows users to be viewed or edited.
    queryset = Given.objects.all()
    serializer_class = GivenSerializer

    @csrf_exempt
    def create(self, request):
        serializer = GivenSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)