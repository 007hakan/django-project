from django.contrib import admin
from .models import Satici

# Register your models here.
class SaticiAdmin(admin.ModelAdmin):
    list_display = ('id','header','text','created_date')
    list_display_links = ('id','header')
    list_filter = ("header",'created_date')
    search_fields = ('header','text')
    list_per_page = 10
admin.site.register(Satici,SaticiAdmin)