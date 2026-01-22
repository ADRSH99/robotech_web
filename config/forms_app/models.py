import uuid
from django.db import models

class Form(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    public_id = models.UUIDField(default=uuid.uuid4, unique=True)
    is_active = models.BooleanField(default=True)


#/f/<uuid>/