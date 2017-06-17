import logging

from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import BasicAuthentication

from app.api.csrf import CsrfExemptSessionAuthentication
from app.api.models.Box import BoxSerializer
from app.api.models.ForAllBox import ForAllBox, ForAllBoxSerializer
from app.api.models.Given import Given, GivenSerializer
from app.api.models.Types import Type, TypeSerializer
from app.api.utils import Z3Exception

@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
class ForAllBoxViewSet(viewsets.ModelViewSet):
    queryset = ForAllBox.objects.all()
    serializer_class = ForAllBoxSerializer

    @csrf_exempt
    def create(self, request, *args, **kwargs):
        logging.error(request.data)
        boxData = dict()
        boxData['proofId'] = request.data.get('proofId')
        boxData['boxId'] = request.data.get('boxId')
        boxData['type'] = request.data.get('type')

        boxSerializer = BoxSerializer(data=boxData)
        if boxSerializer.is_valid(raise_exception=True):
            boxSerializer.save()
        else:
            return Response(boxSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        forallBoxData = dict()
        forallBoxData['variable'] = request.data.get('variable')
        forallBoxData['constant'] = request.data.get('constant')
        forallBoxData['boxId'] = boxSerializer.data.get('id')

        forallBoxSerializer = ForAllBoxSerializer(data=forallBoxData)
        if forallBoxSerializer.is_valid(raise_exception=True):
            forallBoxSerializer.save()
            return Response(boxSerializer.data, status=status.HTTP_200_OK)
        return Response(forallBoxSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        query = ForAllBox.objects.get(boxId=request.query_params['boxId'])
        serializer = ForAllBoxSerializer(query)
        return Response(serializer.data)