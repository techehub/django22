from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse, JsonResponse
from django.template import loader
from pip._internal import req

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



def addItemToCart_old(request):

    vals = request.GET

    qty = vals['qty']
    id = vals['id']

    cartItems=""
    if request.session.__contains__("cart") :
        cartItems=request.session['cart']
        print (cartItems)
        if cartItems:
            cartItems= cartItems+ ","

    cartItems= cartItems+ id+ "|"+qty
    request.session ['cart']= cartItems

    print (request.session ['cart'])

    return HttpResponse("Added Item to Cart")



def addItemToCart(request):
    vals = request.GET
    qty = vals['qty']
    id = vals['id']
    cartItems={}

    if request.session.__contains__("cart") :
        cartItems=request.session['cart']

    cartItems[id] = qty
    request.session ['cart']= cartItems
    print (request.session ['cart'])
    return HttpResponse("Added Item to Cart")


def displaycart(request):
    if request.session.__contains__("cart"):
        cartItems = request.session['cart']
        print(request.session['cart'])
        return HttpResponse(cartItems)
    else :
        return HttpResponse("Your Cart is Empty")



def getProduct(request):
    vals = request.GET
    pid = vals['id']
    product = Product.objects.get(id=pid)

    data = {"id": product.id,
            "name": product.pname,
            "price": product.price}

    return JsonResponse (data)



