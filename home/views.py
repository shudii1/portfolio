# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def projects(request):
    return render(request,'projects.html')


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        cont=Contact(name=name,email=email,phone=phone,desc=desc)
        cont.save()
    return render(request,'contact.html')
