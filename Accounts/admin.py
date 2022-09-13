from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Courses)
admin.site.register(Wishlist)
admin.site.register(Faculty)
admin.site.register(Preferences)
admin.site.register(Batch)