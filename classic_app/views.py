from django.shortcuts import render
from django.template import Context
from .models import Products
import os
from pathlib import Path
from django.http.response import JsonResponse

# Create your views here.

def index(request):
    unique_prod = [prod [0] for prod in Products.objects.all().values_list('productline').distinct()]

    
    return render(request,'index.html',{'cntx':unique_prod})



def getProducts(request):
    prod_list = []
    for product in Products.objects.all():
        try: 
            prod_obj = {} 
            prod_img  = os.listdir(f'classic_app/static/downloads/{product.productname}') 
            prod_obj['productname'] = product.productname 
            prod_obj['productDescription'] = product.productdescription 
            prod_obj['quantityInStock']  = product.quantityinstock 
            prod_obj['msrp'] =  product.msrp 
            prod_obj['product_img'] = list(map(lambda x :f'downloads/{product.productname}/{x}',prod_img))
            prod_list.append(prod_obj) 
            print(prod_obj)
        except Exception as e:
            print('exception happened')
            print(f'classic_app/static/downloads/{product.productname}') 
    return JsonResponse({"products":prod_list})

