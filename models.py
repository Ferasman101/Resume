from django.db import models

# Create your models here.
class Profile(models.Model):

    name= models.CharField(max_length=200)
    mobno= models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    degree= models.CharField(max_length=200)
    school= models.CharField(max_length=200)
    uni= models.CharField(max_length=200)
    summary= models.TextField(max_length=1000)
    previous_work= models.TextField(max_length=1000)
    skills= models.TextField(max_length=1000)