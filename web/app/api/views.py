import logging

from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from app.api.api import GivenSerializer, ProofSerializer
from app.api.models import Given

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
class GivenViewSet(viewsets.ModelViewSet):
        #API endpoint that allows users to be viewed or edited.
    queryset = Given.objects.all()
    serializer_class = GivenSerializer

    @csrf_exempt
    def create(self, request):
        serializer = GivenSerializer(data=request.data)
        logger.error(serializer)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)