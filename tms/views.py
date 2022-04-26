from django.shortcuts import render

from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response

from tms.serializers import ProductSerializer, CategorySerializer
from tms.models import Category, Product


class CategoryList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = ProductSerializer
