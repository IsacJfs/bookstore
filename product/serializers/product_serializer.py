from rest_framework import serializers

from product.models.product import Product, Category
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True, write_only=True, source="category"
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "category",
            "categories_id",
        ]

    def create(self, validated_data):
        # print(validated_data)
        categories_ids = validated_data.pop("category")

        product = Product.objects.create(**validated_data)
        product.category.set(categories_ids)
        return product
