import uuid

from django.db import models

class Proof(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Input(models.Model):
    text = models.CharField(max_length=300)
