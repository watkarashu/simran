from django.db import models

# Create your models here.
class Home(models.Model):
    name=models.CharField(max_length=220)
    mobilenumber=models.CharField(max_length=220)
    email=models.CharField(max_length=220)
    area=models.CharField(max_length=220)