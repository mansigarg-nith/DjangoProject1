from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_master(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=50)