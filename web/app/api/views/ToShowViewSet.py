import logging

from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import BasicAuthentication

from app.api.models.ToShow import ToShow, ToShowSerializer

from app.api.csrf import CsrfExemptSessionAuthentication
logger = logging.getLogger(__name__)

@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
class ToShowViewSet(viewsets.ModelViewSet):
    queryset = ToShow.objects.all()
    serializer_class = ToShowSerializer

    @csrf_exempt
    def create(self, request):
        serializer = ToShowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        query = ToShow.objects.filter(proofId=request.query_params['proofId'])
        serializer = ToShowSerializer(query, many=True)
        return Response(serializer.data)