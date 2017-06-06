import logging

from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import BasicAuthentication

from app.api.csrf import CsrfExemptSessionAuthentication
from app.api.models.Box import BoxSerializer, Box
from app.api.models.Given import Given, GivenSerializer
from app.api.models.Types import Type, TypeSerializer
from app.api.utils import Z3Exception

@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
class BoxViewSet(viewsets.ModelViewSet):
   queryset = Box.objects.all()
   serializer_class = BoxSerializer

   @csrf_exempt
   def create(self, request, *args, **kwargs):
      serializer = BoxSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
         serializer.save()
         return Response(serializer.data, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)