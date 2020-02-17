from django.urls import path
from django.shortcuts import render
from .views import index , getProducts

urlpatterns = [
    path('',index),
    path('getProducts',getProducts)
]