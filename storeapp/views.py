from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Q

from storeapp.models import Product, Category, Order
from storeapp.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status




class Productlistview(APIView):
    
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class Searchitem(APIView):
#     def post(self, request,format=None):
#         product = Product.objects.filter(Q(name =)) 



