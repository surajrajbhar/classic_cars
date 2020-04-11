
from django.urls import path ,include
from django.views.decorators.csrf import csrf_exempt


from rest_framework_simplejwt.views import (
TokenObtainPairView,
    TokenRefreshView,
)

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
   path('rest-auth/', include('rest_auth.urls')),
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]