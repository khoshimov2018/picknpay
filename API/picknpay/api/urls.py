from django.urls import path 

# Write your urls patterns here
from . import views 

urlpatterns = [
    path('buyers', views.buyer, name='createBuyer'),
    path('sellers', views.seller, name='createSeller'), 
    path('items', views.getItems, name='items'),
    path('conditions', views.getTermsAndConditions, name='termsAndConditions')
]