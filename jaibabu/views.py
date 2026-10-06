from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render (request, 'jaibabu/home.html')

def about(request):
    return render(request, 'jaibabu/about.html')

def service(request):
    return render(request,'jaibabu/service.html')

def design(request):
    return render(request,'jaibabu/design.html')

from .models import Contact
def contact(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        message=request.POST.get('message')

        Contact.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            message=message
        )
        messages.success(request,'Thanks for connecting with Us!')
        return redirect('contact')
    return render(request,'jaibabu/contact.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request,"username already exists")
            return redirect('signup')
        
        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request,"account created successfully")
        return redirect('home')
    
    return render(request,'jaibabu/signup.html')




