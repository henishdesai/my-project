from django.db import models # type: ignore

# Create your models here.

class recipe(models.Model):
    name = models.CharField(max_length=100)
    description= models.TextField(max_length=1400)
    image  = models.ImageField(upload_to='recipe')



class contect1(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField(null=True,blank=True)
    contect= models.IntegerField(null=True,blank=True)
    massage=models.TextField(null=True,blank=True)





    










