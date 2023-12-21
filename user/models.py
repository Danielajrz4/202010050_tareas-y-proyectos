from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    DPI = models.BigIntegerField(null=True, blank=True)
    NumCel = models.IntegerField(null=True, blank=True)
