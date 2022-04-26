from rest_framework import serializers

from tms.models import Category, Product


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = '__all__'
