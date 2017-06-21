from django.db import models
from rest_framework import serializers

from app.api.models.Given import Given
from app.api.models.Step import Step


class StepJustification(models.Model):
    step = models.ForeignKey(Step)
    justification = models.ForeignKey(Step)

class StepJustificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepJustification
        fields = ('id', 'step', 'justification')

class GivenJustification(models.Model):
    step = models.ForeignKey(Step)
    justification = models.ForeignKey(Given)

class GivenJustificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GivenJustification
        fields = ('id', 'step', 'justification')