from django.contrib import admin

from .models import Mobile

# Register your models here.

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_filter = ('make', 'is_recommended')
    list_display = ('make', 'name', 'price')

# we can also use decorators to register MobileAdmin class with admin
# admin.site.register(Mobile, MobileAdmin)
