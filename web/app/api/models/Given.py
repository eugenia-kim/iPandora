import sys
sys.path.insert(0, '/Users/eugeniakim/iPandora/theorem_prover')

from django.db import models
from rest_framework import serializers

from app.api.models.Proof import Proof
from Z3StepBuilder import Z3StepBuilder


class Given(models.Model):
    proofId = models.ForeignKey(Proof)
    text = models.CharField(max_length=300)


    @classmethod
    def z3_valid(cls, given, param_map, predicate_map):
        step_builder = Z3StepBuilder(param_map, predicate_map)
        valid = step_builder.visitInput(given)
        return valid

class GivenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Given
        fields = ('id', 'proofId', 'text')
