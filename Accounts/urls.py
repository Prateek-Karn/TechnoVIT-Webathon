from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('adminLogin/', views.adminlogin),
    path('adminhp/', views.adminhp),
]