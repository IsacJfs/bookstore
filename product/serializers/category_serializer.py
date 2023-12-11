from rest_framework import serializers
from django.utils.text import slugify

from product.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug', 'description', 'active']

    def create(self, validated_data):
        # Gerar slug automaticamente a partir do title, se não for fornecido
        validated_data['slug'] = validated_data.get('slug') or slugify(validated_data['title'])
        return super().create(validated_data)