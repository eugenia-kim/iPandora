import uuid
import sys
sys.path.insert(0, '/Users/eugeniakim/iPandora/theorem_prover')

from rest_framework import serializers

from app.api.models.Proof import Proof
from django.db import models

from Z3TypeBuilder import Z3TypeBuilder


class Type(models.Model):
    proofId = models.ForeignKey(Proof)
    text = models.CharField(max_length=300)

    @classmethod
    def is_valid(cls, types):
        type_builder = Z3TypeBuilder(dict(), dict())
        valid = type_builder.visitInputArray(types)
        return valid


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'proofId', 'text')
