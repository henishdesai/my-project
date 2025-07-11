from django.db import models

# Create your models here.

class contect_now(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField(null=True,blank=True)
    massage=models.TextField(null=True,blank=True)

