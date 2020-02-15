from django.shortcuts import render
from django.template import Context
from .models import Products
import os
from pathlib import Path


# Create your views here.

def index(request):
    unique_prod = [prod [0] for prod in Products.objects.all().values_list('productline').distinct()]
    return render(request,'index.html',{'cntx':unique_prod})
