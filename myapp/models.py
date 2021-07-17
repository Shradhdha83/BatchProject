from django.db import models

# Create your models here.

class signup(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=120)
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.IntegerField()

class notes(models.Model):
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    myfile=models.FileField(upload_to='Upload')
    desc=models.TextField()
