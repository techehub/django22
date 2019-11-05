from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse
from django.template import loader
from .models import Product



def productInfo(req):

    vals =req.GET
    pid= vals['id']
    print (pid)

    template=loader.get_template("productinfo.html")

    product = Product.objects.get(id=pid)
    data= {"product":product}
    #data={}
    response= HttpResponse(template.render(data,req))

    cstr= ""
    print (req.COOKIES)
    if "INT_PROD" in req.COOKIES:
        old_ids = req.COOKIES['INT_PROD']
        cstr= old_ids+ "|" + str ( product.id)
    else:
        cstr=product.id

    response.set_cookie("INT_PROD", cstr )

    return response



def productList(req):
    template=loader.get_template("productList.html")

    plist = Product.objects.all()

    data= {

        "products": plist

    }
    return HttpResponse(template.render(data,req))