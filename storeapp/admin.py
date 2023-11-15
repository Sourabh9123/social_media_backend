from django.contrib import admin
from storeapp.models import Product, Category, Address,Customer, Order, OrderItem, Payment


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name","product_price","created_at","updated_at"]
    list_display_links =  ["product_name"]
    prepopulated_fields = {'product_slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_display_links = ['name']
    # prepopulated_fields = {'slug':("name",)}

admin.site.register(Category, CategoryAdmin)


admin.site.register(Customer)

admin.site.register(Address)

admin.site.register(Payment)

admin.site.register(Order)
admin.site.register(OrderItem)
