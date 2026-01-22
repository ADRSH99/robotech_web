from django.db import models
from forms_app.models import Form

class Response(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    answers = models.JSONField()
    submitted_at = models.DateTimeField(auto_now_add=True)
