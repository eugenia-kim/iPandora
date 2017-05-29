import uuid

from django.db import models

class Proof(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Given(models.Model):
    proofId = models.ForeignKey(Proof)
    text = models.CharField(max_length=300)
