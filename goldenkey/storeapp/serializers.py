from typing import Container
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Basket, BasketItem, Category, Content, Order




#Category Serializer
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'



#Content Serializer
class ContentSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source = 'category.title',required=False)

    class Meta:
        model = Content
        fields = '__all__'


#Basket Serializer
class BasketSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source = 'user.email')
    totalPrice = SerializerMethodField()
    items = SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['id','user_email','totalPrice','items']
    
    def get_items(self,obj):
        basketItems = BasketItem.objects.filter(basket = obj)
        return BasketItemSerializer(basketItems, many=True).data

    def get_totalPrice(self,obj):
        return obj.totalPrice


#Basket Items Serializer
class BasketItemSerializer(serializers.ModelSerializer):
    price = SerializerMethodField()
    content = serializers.CharField(source = 'content.title',required = False)

    class Meta:
        model = BasketItem
        fields = ['id','content','quantity','price','date_added']
    
    def get_price(self,obj):
        return obj.price


#Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source = 'user.email',required = False)
    class Meta:
        model = Order
        fields = ['id','user_email','cost','date_added']