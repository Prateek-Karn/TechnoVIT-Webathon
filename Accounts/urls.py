from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('adminLogin/', views.adminlogin),
    path('adminhp/', views.adminhp),
    path('faculty_page/', views.faculty_page),
    path('facultyinfo', views.facultyinfo),
    path('facultyinfoupload/', views.facultyinfoupload),
    path('uploadcoursesadmin/', views.uploadcoursesadmin),
    path('viewaddcourses/', views.viewaddcourses),
    path('viewfacpref/', views.viewfacpref),
    path('wishlistuploadadmin/', views.wishlistuploadadmin),
    path('wishlistviewadmin/', views.wishlistviewadmin),
]