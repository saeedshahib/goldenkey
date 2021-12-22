from django.db.models import query
from django.db.models import F
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import pytz
from rest_framework.response import Response
from storeapp.models import Basket, BasketItem, Category, Content
from storeapp.serializers import BasketItemSerializer, CategorySerializer, ContentSerializer
from .serializers import CustomUserSerializer
from users.models import CustomUser
from rest_framework import generics, pagination, permissions, serializers, status
from django.db.models import Avg
import json
import requests
from datetime import date, datetime
from rest_framework.views import APIView
from rest_framework import filters

# Create your views here.



#Fake credit charge
class CreditCharge(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = get_object_or_404(CustomUser, email = request.user.email)

        #amount of the charge
        amount = request.data['amount']
        instance.cash += amount
        instance.save()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)