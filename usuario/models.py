from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from .managers import UserProfileManager


# Create your models here.

from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    first_name = models.TextField()
    last_name = models.TextField()


    def __str__(self):
        return self.username

# Create your models here.
