from django.urls import path
from django.shortcuts import render
from .views import index , getProducts
from django.views.generic import TemplateView


urlpatterns = [
    path('',index),
    path('getProducts',getProducts),
    path('prodcut_details',TemplateView.as_view(template_name='product_catalog.html'))
]