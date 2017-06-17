from django.db import models
from rest_framework import serializers

from app.api.models.Step import Step


class Justification(models.Model):
    step = models.ForeignKey(Step)
    justification = models.ForeignKey(Step)

class JustificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Justification
        fields = ('id', 'step', 'justification')