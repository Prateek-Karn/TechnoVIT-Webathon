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