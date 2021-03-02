from django.contrib import admin

# Register your models here.

from .models import Buyer, Seller, ItemPurchased, TermsAndCondition 

admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(ItemPurchased)
admin.site.register(TermsAndCondition)

