from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Buyer, Seller, TermsAndCondition, ItemPurchased

class BuyerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buyer
        fields = [
            'id', 
            'username',
            'phone',
            'password', 
            'createdAt', 
            'lastLogin',
            'lastlogout',
            'profilePhoto', 
            'eventAndMarketing',
            'service',
            'personDetails',
        ]

class SellerSerialiazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = [
            'id', 
            'username',
            'phone',
            'password', 
            'createdAt', 
            'lastLogin',
            'lastlogout',
            'profilePhoto', 
            'eventAndMarketing',
            'service',
            'personDetails',
        ]

class TermsAndConditionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TermsAndCondition 
        fields = [
            'conditions'
        ]
class ItemPurchasedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemPurchased 
        fields = [
            'id',
            'name',
            'price',
            'purchasedAt',
            'buyer', 
            'seller',
        ]