from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published' , 'price', 'realtor', 'city')
    list_display_links = ('id', 'name')
    list_filter = ('realtor','name', 'price', 'is_published', 'city')
    list_editable = ('is_published', 'price', 'realtor')
    search_fields = ('name', 'city', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
