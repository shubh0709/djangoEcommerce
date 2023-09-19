from django.contrib import admin

# Register your models here.
from .models import Product, User, Review, ShippingAddress, Order, OrderItem

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)