# Django


# Project
from django.urls import path

from apps.categories.views import CategoryViewSet

urlpatterns = [
    path(r'category', CategoryViewSet.as_view({'get': 'list'}), name='category')
]
