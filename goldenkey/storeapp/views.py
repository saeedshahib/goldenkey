from django.db.models import query
from django.db.models import F
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import pytz
from rest_framework.response import Response
from .models import Basket, BasketItem, Category, Content, Order
from .serializers import BasketItemSerializer, BasketSerializer, CategorySerializer, ContentSerializer, OrderSerializer
from users.models import CustomUser
from rest_framework import generics, pagination, serializers, status
from django.db.models import Avg
import json
import requests
from datetime import date, datetime
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import permissions

# Create your views here.



#Creates a category
class CategoryCreate(generics.CreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer



#Deletes a category
class CategoryDelete(generics.DestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer



#Creates a content with a category by category_id in params
class ContentCreate(generics.CreateAPIView):
	queryset = Content.objects.all()
	serializer_class = ContentSerializer

	def create(self, request, *args, **kwargs):
		category = get_object_or_404(Category, id = request.data['category_id'])
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save(category = category)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




#Adds an item(content) to the basket of the logged in user
class AddItemToBasket(generics.CreateAPIView):
	queryset = BasketItem.objects.all()
	serializer_class = BasketItemSerializer
	permission_classes = [permissions.IsAuthenticated]

	def create(self, request, *args, **kwargs):
		basket = get_object_or_404(Basket, user = request.user)
		content = get_object_or_404(Content, id = request.data['content_id'])
		quantity = request.data['quantity']
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save(basket = basket,content = content,quantity = quantity)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




#Gets the logged in user's basket info
class BasketDetail(generics.RetrieveAPIView):
	queryset = Basket.objects.all()
	serializer_class = BasketSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request, *args, **kwargs):
		instance = get_object_or_404(Basket, user = request.user)
		serializer = self.get_serializer(instance)
		return Response(serializer.data)




#Creates an order with the basket for the logged in user
class OrderBasketItems(generics.CreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	permission_classes = [permissions.IsAuthenticated]

	def create(self, request, *args, **kwargs):
		user = request.user
		basket = get_object_or_404(Basket, user = user)
		basketItems = BasketItem.objects.filter(basket = basket)
		if basketItems.count() == 0:
			return Response({'message' : 'there is no items in your basket'})
		totalPrice = basket.totalPrice

		#drop cash from user after the order
		if user.cash >= totalPrice:
			user.cash -= totalPrice
			user.save()
		else:
			pass #Payment using credit card

		#delete basket items after payment
		basketItems.delete()
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save(user = user, cost = totalPrice)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
