from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # Agrega tus propios campos aquí
    hospital_name = models.CharField(max_length=65)
    pass