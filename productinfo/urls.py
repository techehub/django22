from django.contrib import admin
from django.urls import path
from .views import productInfo, productList, addItemToCart, displaycart


urlpatterns = [
    path ('productInfo', productInfo ),
    path ('productList', productList ),
    path ('addToCart', addItemToCart ),
    path('cart', displaycart)

]
