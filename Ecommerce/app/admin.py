from django.contrib import admin
from . models import *
# Register your models here.

@admin.register((person))
class personModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message']

@admin.register((product))    
class productModelAdmin((admin.ModelAdmin)):
    list_display = ['id','discrition','upload_img']   