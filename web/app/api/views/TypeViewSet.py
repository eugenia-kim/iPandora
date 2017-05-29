import logging

from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import BasicAuthentication

from app.api.models.Types import Type, TypeSerializer

from app.api.csrf import CsrfExemptSessionAuthentication
logger = logging.getLogger(__name__)

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