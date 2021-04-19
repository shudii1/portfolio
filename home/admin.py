from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'phone']
    list_filter = ['email', 'name']


admin.site.register(Contact, ContactAdmin)
