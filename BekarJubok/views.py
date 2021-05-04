from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView,ListView
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import JobCategory, JObDescription, Employee
from django.db.models import Q


def navbar(request):
    category = JobCategory.objects.all()
    jobs = JObDescription.objects.all()
    employee = Employee.objects.all()
    return render(request,'BekarJubok/base.html',{'category':category,'jobs':jobs,'employee':employee})

def register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        user = User.objects.create_user(username=username,email=email,password=pass1)
        user.save()
        print("User Created")
        return redirect('/')
    else:
        print("Failed try again")
        return render(request,'BekarJubok/Register.html')

def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("User Logged in")
            return redirect("/")

        else:
            print("ohh no")
            messages.info(request,'invalid credentials')
            return redirect("login")
    
    else:
        print("Login Unsuccessful")
        return render(request,'BekarJubok/login.html')

def logout(request):
    print("user logged out")
    auth.logout(request)
    return redirect("/")

def search(request):
    query = request.GET.get('keyword')
    company = JObDescription.objects.filter(company__contains=query)
    #category = JObDescription.objects.filter(jobcategory__contains=query)
    position = JObDescription.objects.filter(position__contains=query)
    skills = JObDescription.objects.filter(skills__contains=query)
    deadline = JObDescription.objects.filter(app_dedline__contains=query)
    circular = company.union(position)#
    return render(request,'BekarJubok/search_results.html',{'circular':circular})
