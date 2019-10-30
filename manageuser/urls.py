from django.contrib import admin
from django.urls import path
from .views import registerUser


urlpatterns = [
    path ('register', registerUser ),
]
