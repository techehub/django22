from django.shortcuts import render
from django.template import loader
# Create your views here.
from .forms import UserReg

from django.http import  HttpResponse


def registerUser(request):
    template = loader.get_template("userreg.html")
    userForm= UserReg()
    data= { "myform": userForm}
    return HttpResponse(template.render(data, request))

def saveUserDetails(request):
    data=request.GET
    print (data['firstName'])
    print(data['lastName'])
    return HttpResponse("done")