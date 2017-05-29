from django.db import models
from rest_framework import serializers

from app.api.models.Proof import Proof


class Given(models.Model):
    proofId = models.ForeignKey(Proof)
    text = models.CharField(max_length=300)

class GivenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Given
        fields = ('id', 'proofId', 'text')
