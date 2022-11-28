# Rest framework
from rest_framework import serializers

from apps.authors.models import Author
from apps.categories.models import Category
from apps.products.models import Product


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name"
        ]


class ProductAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "name"
        ]


class ProductSerializer(serializers.ModelSerializer):
    author = ProductAuthorSerializer(many=False)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "author",
            "year",
            "language",
            "image",
            "created_date",
            "last_update"
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(many=True)
    author = ProductAuthorSerializer(many=False)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "author",
            "description",
            "file",
            "image",
            "video",
            "language",
            "year",
            "size",
            "size_type",
            "file_type"
        ]
