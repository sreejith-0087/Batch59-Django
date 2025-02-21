from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Details)


class UserAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Age', 'Subject', 'Email']
    list_editable = ['Subject', 'Email']
    search_fields = ['Name', 'Subject']
admin.site.register(UserModel, UserAdmin)



@admin.register(InfoModel)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Address', 'Phone']
    list_editable = ['Email', 'Address', 'Phone']
    search_fields = ['Name', 'Email', 'Address', 'Phone']




