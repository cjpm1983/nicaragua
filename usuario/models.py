from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from .managers import UserProfileManager

from django.contrib.auth.models import AbstractUser


# Create your models here.

from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    pasaporte = models.CharField(max_length=7,null=True) 

    def __str__(self):
        return self.username


