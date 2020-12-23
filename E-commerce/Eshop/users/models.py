from django.db import models

class UserModel(models.Model):
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)


# Create your models here.
