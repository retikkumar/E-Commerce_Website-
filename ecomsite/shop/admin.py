from django.contrib import admin
from .models import MyCart, Products,Order
# Register your models here.
admin.site.site_header = "E-commerce site"
admin.site.index_title = "Manage shop"
admin.site.site_title = "Shop"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description = 'Default category'
    list_display = ('title','price','discount_price','category','description')
    actions = ('change_category_to_default',)
    search_fields = ('title',)
    list_editable = ('price','discount_price',)
  
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
admin.site.register(MyCart)