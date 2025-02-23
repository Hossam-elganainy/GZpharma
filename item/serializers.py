from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        if isinstance(validated_data, list):
            return Item.objects.bulk_create([Item(**item) for item in validated_data])
        return super().create(validated_data)