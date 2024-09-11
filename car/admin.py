from django.contrib import admin

# Register your models here.
from .models import Car, Comment

admin.site.register(Car)
admin.site.register(Comment)