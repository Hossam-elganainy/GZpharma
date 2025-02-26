from django.urls import path, include
from .views import ItemList, ItemDetail, ItemDestroyAll

urlpatterns = [
    path('', ItemList.as_view(), name='items'),
    path('<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('delete-all/', ItemDestroyAll.as_view(), name='items-delete-all'),
]