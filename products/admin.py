from django.contrib import admin
from django.forms import forms

# Register your models here.

from .models import products


class displayproducts (admin.ModelAdmin):
    list_display=("name","price","stock" )



admin.site.register(products, displayproducts)