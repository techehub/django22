from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse


def productInfo(req):
    return HttpResponse("This is my product info page ")