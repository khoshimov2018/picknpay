from django.urls import include, path
from rest_framework import routers
from api import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'buyers', views.BuyerViewSet)
router.register(r'sellers', views.SellerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]