from django.shortcuts import render,HttpResponse

# Create your views here.
def home_view(request):
    return render(request,"CAN/home.html")


def employe_view(request):
    return render(request,"CAN/emplye_custmer.html")


def order_book(request):
    return render(request,"CAN/order.html")


def contact_view(request):
    return render(request,"CAN/contact.html")




    