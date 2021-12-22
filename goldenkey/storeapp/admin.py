from django.contrib import admin

from .models import Basket, BasketItem, Category, Content, Order

# Register your models here.

admin.site.register(Category)
admin.site.register(Content)
admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(Order)