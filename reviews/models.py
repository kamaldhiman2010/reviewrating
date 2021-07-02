from django.core import validators
from django.db import models


class User(models.Model):

    image= models.FileField(upload_to="images",blank=True,null=True)
    company=models.CharField(max_length=70)
    username=models.CharField(max_length=70)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=100,null=True)
    about_me=models.CharField(max_length=100)



    def upload_photo_dir(self, filename):
        path = '/media/images/{}'.format(filename)
        return path
    #image= models.ImageField(upload_to=upload_photo_dir)


    def __str__(self):
        return self.username
class Login(models.Model):
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=50)

# Create your models here.
