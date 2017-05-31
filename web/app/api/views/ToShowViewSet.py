import logging

from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import BasicAuthentication

from app.api.models.ToShow import ToShow, ToShowSerializer

from app.api.csrf import CsrfExemptSessionAuthentication
from app.api.models.Types import TypeSerializer, Type
from app.api.utils import Z3Exception

logger = logging.getLogger(__name__)

@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
class ToShowViewSet(viewsets.ModelViewSet):
    queryset = ToShow.objects.all()
    serializer_class = ToShowSerializer

    @csrf_exempt
    def create(self, request):
        serializer = ToShowSerializer(data=request.data)
        if serializer.is_valid():
            type_query = Type.objects.filter(proofId=request.data['proofId'])
            types = [t['text'] for t in TypeSerializer(type_query, many=True).data]
            type_valid, param_map, predicate_map = Type.get_maps(types)
            if not type_valid:
                raise Z3Exception('Type Declarations Error', 'text', status.HTTP_400_BAD_REQUEST)
            try:
                step_valid = ToShow.is_valid(serializer.validated_data['text'], param_map, predicate_map)
            except Exception as err:
                raise Z3Exception(err, 'text', status.HTTP_400_BAD_REQUEST)
            if not step_valid:
                raise Z3Exception('Syntax Error', 'text', status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        query = ToShow.objects.filter(proofId=request.query_params['proofId'])
        serializer = ToShowSerializer(query, many=True)
        return Response(serializer.data)