from django.contrib import admin

# Register your models here.

from .models import Event
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['eventTitle', 'eventdesc']
    list_filter = []
    search_fields = ['eventTitle']
