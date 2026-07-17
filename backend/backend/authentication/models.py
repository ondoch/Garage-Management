from django.db import models
from .usermanager import UserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(
        'Email address',
        unique=True
    )

    first_name = models.CharField(
        max_length=255
    )
    
    last_name = models.CharField(
        max_length=255
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    