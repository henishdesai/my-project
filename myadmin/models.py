from django.db import models

# Create your models here.


class admin_user(models.Model):
    amd_name = models.CharField(max_length=20)
    amd_password = models.CharField(max_length=200)
    amd_email = models.EmailField(max_length=20)
    amd_status = models.BooleanField(default=True)

class CategoryMaster(models.Model):
    catName   = models.CharField(max_length=100)
    catImage  = models.ImageField(upload_to="catagory_images")
    catStatus = models.BooleanField(default=True,null=False)
    catSlug   = models.SlugField()
   



