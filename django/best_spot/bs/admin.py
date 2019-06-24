from django.contrib import admin
from .models import BS

class BSAdmin(admin.ModelAdmin):
    list_display = ('year','month','day','hour','min','title','member','weight','start','goal')

admin.site.register(BS, BSAdmin)