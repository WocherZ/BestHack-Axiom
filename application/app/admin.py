from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    pass


class StockAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PropertiesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stock, StockAdmin)
admin.site.register(Properties, PropertiesAdmin)
