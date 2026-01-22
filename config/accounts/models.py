# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('WEB', 'Web Lead'),
        ('CONV', 'Convener'),
        ('SIG', 'SIG Head'),
        ('GEN', 'General'),
    )
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='GEN')
