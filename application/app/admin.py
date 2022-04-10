from django.contrib import admin

from .models import User, Stock, Properties


class UserAdmin(admin.ModelAdmin):
    pass


class StockAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PropertiesAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Properties, PropertiesAdmin)
