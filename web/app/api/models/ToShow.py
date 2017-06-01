import sys
sys.path.insert(0, '/Users/eugeniakim/iPandora/theorem_prover')
from rest_framework import serializers

from app.api.models.Proof import Proof
from django.db import models

from Z3StepBuilder import Z3StepBuilder

class ToShow(models.Model):
    proofId = models.ForeignKey(Proof)
    text = models.CharField(max_length=300)

    @classmethod
    def z3_valid(cls, toshow, param_map, predicate_map):
        step_builder = Z3StepBuilder(param_map, predicate_map)
        valid = step_builder.visitInput(toshow)
        return valid

class ToShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToShow
        fields = ('id', 'proofId', 'text')
