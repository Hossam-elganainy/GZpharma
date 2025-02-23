from django.urls import path, include
from .views import ItemList, ItemDetail

urlpatterns = [
    path('', ItemList.as_view(), name='items'),
    path('<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]

