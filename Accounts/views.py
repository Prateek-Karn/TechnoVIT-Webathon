from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    return render(request,'Accounts/index.html') #index

def adminlogin(request):
    return render(request,'Accounts/adminlogin.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('adminLogin')



    else:
        return render(request, 'adminhp.html')

def adminhp(request):
    return render(request,'Accounts/adminhp.html')

def faculty_page(request):
    return render(request,"Accounts/faculty_page.html")

def facultyinfo(request):
    return render(request,'Accounts/facultyinfo.html')
        
def facultyinfoupload(request):
    return render(request,'Accounts/facultyinfoupload.html')

def uploadcoursesadmin(request):
    return render(request,'Accounts/uploadcoursesadmin.html')

def viewaddcourses(request):
    return render(request,'Accounts/viewaddcourses.html')

def viewfacpref(request):
    return render(request,'Accounts/viewfacpref.html')

def wishlistuploadadmin(request):
    return render(request,'Accounts/wishlistuploadadmin.html')

def wishlistviewadmin(request):
    return render(request,'Accounts/wishlistviewadmin.html')

