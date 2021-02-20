from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BuyersSerializer, SellersSerialiazer


from .models import Buyers, Sellers

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyers.objects.all()
    serializer_class = BuyersSerializer 
    permissions_classes = [permissions.IsAuthenticated]

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Sellers.objects.all()
    serializer_class = SellersSerialiazer
    permissions_classes = [permissions.IsAuthenticated]
