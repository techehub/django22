from django.contrib import admin
from django.urls import path
from .views import productInfo, productList, addItemToCart, displaycart, getProduct


urlpatterns = [
    path ('productInfo', productInfo ),
    path ('productList', productList ),
    path ('addToCart', addItemToCart ),
    path('cart', displaycart),
    path('product', getProduct)

]
