from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Buyers, Sellers

class BuyersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buyers
        fields = [
            'phone', 
            'password', # hashed password
            'createAt',
            'items_puchased',
            'lastLogin',
            'logoutAt'
        ]


class SellersSerialiazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sellers
        fields = [
            'phone', 
            'password', # hashed password
            'createAt',
            'items_puchased',
            'lastLogin',
            'logoutAt'
        ]
