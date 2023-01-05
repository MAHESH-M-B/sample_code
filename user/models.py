from django.db import models
# Create your models here.
class user(models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10, blank=False, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)