from django.contrib import admin
from .models import Category, Facility, Service, Background_Image, About
# Register your models here.
admin.site.register(Category)
admin.site.register(Facility)
admin.site.register(Service)
admin.site.register(Background_Image)
admin.site.register(About)
