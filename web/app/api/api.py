from rest_framework import serializers, viewsets

from .models import Input, Proof


class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Input
        fields = ('id', 'text')

class ProofSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proof
        fields = ('id',)

