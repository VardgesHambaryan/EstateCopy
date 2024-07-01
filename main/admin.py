from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    list_display_links = ['name', 'email', 'phone']

