from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.IntegerField(null=True)
    city=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=100)
