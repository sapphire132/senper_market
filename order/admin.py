from django.contrib import admin

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('client','item','phone','email','amount')
    list_display_links = ('client','item')
    search_fields = ('clients','item','phone')
    list_per_page = 25


admin.site.register(Order, OrderAdmin)
