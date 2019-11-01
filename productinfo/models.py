from django.db import models

# Create your models here.

class Product (models.Model):
    pid = models.CharField(max_length=10)
    pname= models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    price= models.IntegerField()
    features = models.CharField(max_length=500)
    mdate= models.DateField()

