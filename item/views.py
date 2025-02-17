from django.shortcuts import render
from .models import Item
from .serializers import ItemSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ItemFilter
from rest_framework.permissions import IsAuthenticated
class ItemList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilter





