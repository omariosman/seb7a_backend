from django.contrib import admin

from .models import Zekr
# Register your models here.

    

class ZekrAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Zekr, ZekrAdmin)