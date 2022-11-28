# Django REST framework
from rest_framework import viewsets

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    search_fields = ('name', )
    ordering_fields = ('name', 'created_date')
