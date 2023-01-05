from django.db import models
# Create your models here.
class Form(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    age=models.IntegerField()
    queries=models.TextField()
