from django.shortcuts import render

from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response

from tms.serializers import ProductSerializer, CategorySerializer, CartSerializer, AddCartProduct
from tms.models import Category, Product, Cart


class CategoryList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewsSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class AddCart(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = AddCartProduct

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instanse = serializer.save()
        serializer = CartSerializer(instance=instanse)
        return Response(serializer.data)

"""
метод POST
проверяем есть ли корзина
если нет - создаем 
добавляем продукт
"""
