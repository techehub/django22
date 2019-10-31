from django.contrib import admin
from django.urls import path
from .views import productInfo, productList


urlpatterns = [
    path ('productInfo', productInfo ),
    path ('productList', productList ),
]
