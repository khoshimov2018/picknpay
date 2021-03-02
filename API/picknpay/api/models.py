from django.db import models

# Create your models here.

class Buyer(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    createdAt = models.DateField(auto_now_add=True) 
    lastLogin = models.DateField(null=True)
    lastlogout = models.DateField(null=True)
    profilePhoto = models.BooleanField(default=False)
    eventAndMarketing = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    personDetails = models.BooleanField(default=False)
    
class Seller(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=20, default='01082930455')
    createdAt = models.DateField(auto_now_add=True)
    lastLogin = models.DateField(null=True)
    lastlogout = models.DateField(null=True)
    profilePhoto = models.BooleanField(default=False)
    eventAndMarketing = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    personDetails = models.BooleanField(default=False)

class ItemPurchased(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField() 
    purchasedAt = models.DateField(auto_now_add=True) 
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

class TermsAndCondition(models.Model):
    conditions = models.TextField()
