from django.contrib import admin
from core.models import *

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'path')

@admin.register(Device)
class DevicetAdmin(admin.ModelAdmin):
    list_display = ('device_name',)

admin.site.register(Employee)
admin.site.register(Student)

# Register your models here.
