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

    @classmethod
    def get_maps(cls, types):
        param_map = dict()
        predicate_map = dict()
        type_builder = Z3TypeBuilder(param_map, predicate_map)
        valid = type_builder.visitInputArray(types)
        return valid, param_map, predicate_map


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'proofId', 'text')
