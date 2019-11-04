from django.contrib import admin
from django.urls import path
from .views import registerUser,saveUserDetails


urlpatterns = [
    path ('register', registerUser ),
    path('saveUser', saveUserDetails),

]
