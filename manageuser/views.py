from django.shortcuts import render

# Create your views here.


from django.http import  HttpResponse


def registerUser(request):
    return HttpResponse("This is my register page")