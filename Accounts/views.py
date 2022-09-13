from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'Accounts/index.html') #index

def adminlogin(request):
    return render(request,'Accounts/adminlogin.html')

def adminhp(request):
    return render(request,'Accounts/adminhp.html')

def faculty_page(request):
    return render(request,"Accounts/faculty_page.html")

def facultyinfo(request):
    return render(request,'Accounts/facultyinfo.html')
        
def facultyinfoupload(request):
    return render(request,'Accounts/facultyinfoupload.html')

def uploadcoursesadmin(request):
    return render(request,'Accounts/uploadcourseadmin.html')

def viewaddcourses(request):
    return render(request,'Accounts/viewaddcourses.html')

def viewfacpref(request):
    return render(request,'Accounts/viewfacpref.html')

def wishlistuploadadmin(request):
    return render(request,'Accounts/wishlistuploadadmin.html')

def wishlistviewadmin(request):
    return render(request,'Accounts/wishlistviewadmin.html')

