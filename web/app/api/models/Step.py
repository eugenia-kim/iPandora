from rest_framework import serializers

from app.api.models.Box import Box
from app.api.models.Given import Given
from django.db import models

from Z3StepBuilder import Z3StepBuilder
from Z3ProofBuilder import Z3ProofBuilder

from app.api.models.Proof import Proof


class Step(models.Model):
    proofId = models.ForeignKey(Proof)
    text = models.CharField(max_length=300)
    given_just = models.ManyToManyField(Given, blank=True, null=True)
    step_just = models.ManyToManyField("self", blank=True, null=True)
    boxId = models.ForeignKey(Box, blank=True, null=True)
    depth = models.IntegerField(default=0)
    isFirstStepInBox = models.BooleanField(default=False)

    @classmethod
    def z3_valid(cls, step, param_map, predicate_map):
        step_builder = Z3StepBuilder(param_map, predicate_map)
        valid, _ = step_builder.visitInput(step)
        return valid, step_builder

    @classmethod
    def proof_valid(cls, step_builder, step, given_just, step_just):
        proof_builder = Z3ProofBuilder(step_builder, step, given_just, step_just)
        return proof_builder.isValid()

    @classmethod
    def proof_sat(cls, step_builder, step, given_just, step_just):
        proof_builder = Z3ProofBuilder(step_builder, step, given_just, step_just)
        return proof_builder.isSat()

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'proofId', 'text', 'given_just', 'step_just', 'boxId', 'depth', 'isFirstStepInBox')
