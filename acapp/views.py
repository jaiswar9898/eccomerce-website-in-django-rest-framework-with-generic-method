from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Category, Book, Product
from .serializers import  CategorySerializer, BookSerializer, ProductSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid

class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListBook(generics.ListCreateAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
  
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ListProduct(generics.ListCreateAPIView):    
  
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


