from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class User_Info(models.Model):
    user = models.OneToOneField(User)
    middle_name = models.CharField(max_length=10)
    def __str__(self):
        return self.user.username