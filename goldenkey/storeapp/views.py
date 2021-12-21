from django.db.models import query
from django.db.models import F
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import pytz
from rest_framework.response import Response
from goldenkey.storeapp.models import BasketItem
from goldenkey.storeapp.serializers import BasketItemSerializer
from users.models import CustomUser
from rest_framework import generics, pagination, serializers, status
from django.db.models import Avg
import json
import requests
from datetime import date, datetime
from rest_framework.views import APIView
from rest_framework import filters

# Create your views here.


class AddItemToBasket(generics.CreateAPIView):
	queryset = BasketItem.objects.all()
	serializer_class = BasketItemSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)