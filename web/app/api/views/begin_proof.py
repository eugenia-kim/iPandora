import logging

from django.shortcuts import redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from app.api.csrf import CsrfExemptSessionAuthentication

from app.api.models.Proof import ProofSerializer

logger = logging.getLogger(__name__)

@api_view(['POST'])
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def begin_proof(request):
    serializer = ProofSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        return redirect('/' + str(instance.id))
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)