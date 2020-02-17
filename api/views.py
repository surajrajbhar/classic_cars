from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny 
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from classic_app.models import Orders,Payments , Customers , Orderdetails , Products
from .serializers import OrdersSerializer , ProductsSerializer ,PaymentsSerializer , UserSerializer , OrderdetailsSerializer
from django.contrib.auth.models import User


class OrdersViewset(viewsets.ModelViewSet):
    queryset =  Orders.objects.all()
    serializer_class =  OrdersSerializer
    #permission_classes = [IsAuthenticated]


    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     if request.user=='AnonymousUser':
    #         return Response(f'response:{request.user}')
    #     print(f'request : {request.user}')
    #     customer_number = Customers.objects.filter(contactfirstname__contains=str(request.user).split('_')[0]).values_list('customernumber')[0]
    #     order_details = Orders.objects.filter(customernumber=customer_number)
    #     serialized_orders =  OrdersSerializer(order_details,many=True).data        
    #     return Response(serialized_orders)

    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



class UserViewset(viewsets.ModelViewSet):
    queryset =   User.objects.all()
    serializer_class = UserSerializer


class PaymentViewset(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

class OrderDetailsViewset(viewsets.ModelViewSet):
    queryset =  Orderdetails.objects.all()
    serializer_class =  OrderdetailsSerializer


class OrderDetailsViewset(viewsets.ModelViewSet):
    queryset =  Orderdetails.objects.all()
    serializer_class =  OrderdetailsSerializer
    



class ProductsDetailsViewset(viewsets.ModelViewSet):
    queryset =  Products.objects.all()
    serializer_class =  ProductsSerializer
    
    