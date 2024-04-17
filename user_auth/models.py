from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Form(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    email = models.EmailField()
    signup_confirmation = models.BooleanField(default=False)



