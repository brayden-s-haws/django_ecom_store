from django.contrib import admin
from .models import Product, Order

# Register your models here.
admin.site.site_header = "Ecommerce Site"
admin.site.site_title = "Ecommerce Administration"
admin.site.index_title = "Manage Ecommerce Site"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')

    change_category_to_default.short_description = "Default Category"
    list_display = ('name', 'price', 'category', 'description')
    search_fields = ('name', 'description')
    list_filter = ('category',)
    actions = ['change_category_to_default',]
    fields = ('name', 'price', 'category', 'description')
    list_editable = ('price', 'category')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)