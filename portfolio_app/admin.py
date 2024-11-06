from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_number','description')
    search_fields = ('name', 'email', 'mobile_number','description')


