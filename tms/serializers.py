from django.contrib.auth.models import User
from rest_framework import serializers

from tms.models import Category, Product, Cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Cart
        fields = '__all__'


class AddCartProduct(serializers.ModelSerializer):

    product = serializers.IntegerField(write_only=True)

    class Meta:
        model = Cart
        fields = ('product',)

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs

    def create(self, validated_data):
        cart = Cart.objects.filter(user=validated_data['user']).first()

        if cart:
            cart.product.add(validated_data['product'])
        if not cart:

            cart = Cart.objects.create(user=validated_data['user'])
            cart.product.add(validated_data['product'])

        # breakpoint()
        #
        # serializer = CartSerializer(instance=cart)
        return cart
