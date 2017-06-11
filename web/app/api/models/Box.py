import uuid

from django.db import models
from rest_framework import serializers

from app.api.models.Proof import Proof

class Box(models.Model):
    proofId = models.ForeignKey(Proof)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parentId = models.ForeignKey("self", blank=True, null=True)

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ('id', 'proofId', 'parentId',)
