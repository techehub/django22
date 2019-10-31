from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse
from django.template import loader


def productInfo(req):
    template=loader.get_template("productinfo.html")
    data= {"name": "VIVO",
           "desc": " Smart Phone",
           "price": 45555}
    return HttpResponse(template.render(data,req))



def productList(req):
    template=loader.get_template("productList.html")
    data= {

        "products": [{"name": "VIVO",
           "desc": " Smart Phone",
           "price": 45555},

         {"name": "OPPO",
               "desc": " Smart Phone",
               "price": 50000,
               "feature": ["8GB RAM", "30 MP Camera", "6 Inch Display"]},

        {"name": "Samsung",
               "desc": " Smart Phone",
               "price": 30000,
            "feature": ["4GB RAM", "20 MP Camera", "5 Inch Display"]},


         ]

    }
    return HttpResponse(template.render(data,req))