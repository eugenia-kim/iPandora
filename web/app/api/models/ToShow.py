import uuid

from rest_framework import serializers

from app.api.models.Proof import Proof
from django.db import models

class ToShow(models.Model):
    proofId = models.ForeignKey(Proof)
    text = models.CharField(max_length=300)

class ToShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToShow
        fields = ('id', 'proofId', 'text')
