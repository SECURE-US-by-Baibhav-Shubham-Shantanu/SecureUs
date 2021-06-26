from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)