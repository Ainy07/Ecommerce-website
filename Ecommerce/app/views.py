from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from . models import *
from django.contrib import messages



def home(request):
    item = product.objects.all()
    return render(request, "home.html",
                    {"item":item})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def contact_us(request):
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    u = person.objects.create(name=name, email=email,
                              subject=subject, message=message)
    
    messages.success(request, "registration successfully")
    return redirect('/contact/')
