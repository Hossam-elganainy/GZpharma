from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Item
from .serializers import ItemSerializer
from .filters import ItemFilter

class ItemList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilter

    def create(self, request, *args, **kwargs):
        is_bulk = isinstance(request.data, list)  # Check if data is a list
        serializer = self.get_serializer(data=request.data, many=is_bulk)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
