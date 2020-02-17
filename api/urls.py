
from django.urls import path ,include

from rest_framework import routers
from api.views import OrdersViewset , UserViewset , PaymentViewset , OrderDetailsViewset ,ProductsDetailsViewset

router = routers.DefaultRouter()
router.register(r'orders', OrdersViewset)
router.register(r'users',UserViewset)
router.register(r'payments',PaymentViewset)
router.register(r'order_details',OrderDetailsViewset)
router.register(r'products',ProductsDetailsViewset)




urlpatterns = [
   path('', include(router.urls)),
   path('auth/', include('rest_auth.urls')),

]