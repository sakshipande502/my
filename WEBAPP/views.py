from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactForm
from datetime import datetime
from django.contrib import messages


# Create your views here.



def index(request):
    return render(request,'WEBAPP/index.html')

def about(request):
    return render(request,'WEBAPP/about.html')

def contact(request):
    if request.method== "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contactform = ContactForm(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contactform.save()
        messages.success(request,"message has been sent")
    return render(request,'WEBAPP/contact.html')

def education(request):
    return render(request,'WEBAPP/education.html')


