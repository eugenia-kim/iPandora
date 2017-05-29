import uuid

from django.db import models
from rest_framework import serializers


class Proof(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class ProofSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proof
        fields = ('id',)