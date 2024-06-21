from django.contrib import admin

from pages.models import Company, Department, Employee

# Register your models here.
admin.site.register( Company )
admin.site.register( Department )
admin.site.register( Employee )
