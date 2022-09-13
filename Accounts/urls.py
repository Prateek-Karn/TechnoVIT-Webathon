from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminLogin/', views.adminlogin,name='adminLogin'),
    path('adminhp/', views.adminhp, name='adminhp'),
    path('faculty_page/', views.faculty_page,name='faculty_page'),
    path('facultyinfo', views.facultyinfo,name='facultyinfo'),
    path('facultyinfoupload/', views.facultyinfoupload, name='facultyinfoupload'),
    path('uploadcoursesadmin/', views.uploadcoursesadmin,name='uploadcoursesadmin'),
    path('viewaddcourses/', views.viewaddcourses, name='viewaddcourses'),
    path('viewfacpref/', views.viewfacpref, name='viewfacpref'),
    path('wishlistuploadadmin/', views.wishlistuploadadmin, name='wishlistuploadadmin'),
    path('wishlistviewadmin/', views.wishlistviewadmin, name='wishlistviewadmin'),

]