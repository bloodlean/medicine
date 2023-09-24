from django.contrib import admin
from .models import Client, Blog, Sponsor

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')
    list_display_links = ('full_name', 'phone_number')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_display_links = ('title', 'date')

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    list_display_links = ('name', 'image')