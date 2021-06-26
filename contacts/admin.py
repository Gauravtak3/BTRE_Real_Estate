from django.contrib import admin

from .models import Contacts

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','listing','email','contacts_date')
    list_display_links = ('id','name')
    search_fields = ('name','email','listing')
    list_per_page = 20

admin.site.register(Contacts, ContactAdmin)

