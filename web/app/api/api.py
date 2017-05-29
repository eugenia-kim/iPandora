from rest_framework import serializers, viewsets

from .models import Proof, Given

class GivenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Given
        fields = ('id', 'proofId', 'text')

class ProofSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proof
        fields = ('id',)

