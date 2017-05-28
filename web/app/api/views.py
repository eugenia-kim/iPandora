import logging

from django.shortcuts import redirect
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from app.api.api import InputSerializer, ProofSerializer
from app.api.models import Input

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

class InputViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = Input.objects.all()
    serializer_class = InputSerializer
