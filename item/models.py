from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.FloatField()
    sheetName = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
    
    
    
