import logging

from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import BasicAuthentication

from app.api.csrf import CsrfExemptSessionAuthentication
from app.api.models.Given import Given, GivenSerializer

logger = logging.getLogger(__name__)

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