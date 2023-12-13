from rest_framework import serializers
from order.models.order import Order

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True, write_only=True
    )
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Order
        fields = ["product", "total", "user", "products_id"]
        extra_kwargs = {"product": {"required": False}}

    def create(self, validated_data):
        products = validated_data.pop("products_id")
        user_data = validated_data.pop("user")

        order = Order.objects.create(user=user_data)
        order.product.set(products)
        return order
