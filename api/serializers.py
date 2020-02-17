from rest_framework import serializers
from classic_app.models import Orders,Payments , Orderdetails ,Products

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password','is_superuser','is_staff')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    



class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'



class OrderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Orderdetails
        fields =  '__all__'




class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Products
        fields =  '__all__'
    