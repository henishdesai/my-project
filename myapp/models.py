from django.db import models # type: ignore

# Create your models here.


class student(models.Model):
    name = models.CharField(default= None, max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField(null=True, blank=True)
    addres = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class year(models.Model):
     name = models.CharField(default= None, max_length=100)
     price = models.IntegerField(default=0)
    