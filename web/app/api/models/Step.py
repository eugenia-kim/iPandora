from app.api.models import Given
from django.db import models

class Step(models.Model):
    proofId = models.ForeignKey(Proof)
    text = models.CharField(max_length=300)
    given_just = models.ManyToManyField(Given)
    step_just = models.ManyToManyField("self")
