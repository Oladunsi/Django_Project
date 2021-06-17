from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Portfolio(models.Model):
    title = User.objects.filter(username="Oladunsi")

    def __str__(self):
        return self.title