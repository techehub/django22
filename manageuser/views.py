from django.shortcuts import render
from django.template import loader
# Create your views here.
from .forms import UserReg
from .models import User


from django.http import  HttpResponse


def registerUser(request):
    template = loader.get_template("userreg.html")
    userForm= UserReg()
    data= { "myform": userForm}
    return HttpResponse(template.render(data, request))

def saveUserDetails(request):

    print (request.method)

    if request.method=='POST':
        data=request.POST

    else :
        data = request.GET

    fname= data['firstName']
    lname= data['lastName']
    email= data['emailName']
    pwd = data['password']

    user = User()
    user.fname=fname
    user.lname=lname
    user.email=email
    user.pwd=pwd
    user.save()

    return HttpResponse("done")

def logoutUser(request):
    request.session.clear()
    return HttpResponse("Logged out")