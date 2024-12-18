from django.shortcuts import render
from .models import carsList

def index(request):
    car=carsList.objects.all()
    return render(request,"index.html",{"car":car})

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def pricing(request):
    return render(request,"pricing.html")

def car(request):
    carL=carsList.objects.all()
    for i in carL:
        print("car image 1",i.carimage.url)
        print("car image 2",i.carimage)
    return render(request,"car.html",{"carL":carL})

def car_Single(request):
    return render(request,"car-single.html")

def blog(request):
    return render(request,"blog.html")

def blog_Single(request):
    return render(request,"blog-single.html")

def contact(request):
    return render(request,"contact.html")

def main(request):
    return render(request,"main.html")

def trial(request):
    cars_list = carsList.objects.all()
    return render(request, "trial.html", {'cars': cars_list})



# Create your views here.
