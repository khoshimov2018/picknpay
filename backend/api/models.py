from django.db import models

# Create your models here.
class Buyers(models.Model):
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    createAt = models.DateTimeField()
    logoutAt = models.DateTimeField()
    lastLogin = models.DateTimeField()
    items_puchased = models.IntegerField()

class Sellers(models.Model):
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    createAt = models.DateTimeField()
    logoutAt = models.DateTimeField()
    lastLogin = models.DateTimeField()

