from django.db import models
from rest_framework import serializers

from app.api.models.Box import Box


class ForAllBox(models.Model):
    boxId = models.ForeignKey(Box)
    variable = models.CharField(max_length=10)
    constant = models.CharField(max_length=10)

class ForAllBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForAllBox
        fields = ('id', 'boxId', 'variable', 'constant', )