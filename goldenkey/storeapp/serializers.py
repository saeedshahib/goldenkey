from typing import Container
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from goldenkey.storeapp.models import Basket, BasketItem, Category, Content





class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'



class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = '__all__'


class BasketItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = '__all__'