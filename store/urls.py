from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='store_index'),
    path('search', views.search, name='store_search'),
    path('details/<int:id>', views.details, name='store_details'),
    path('add-to-basket/<int:id>', views.add_to_basket, name='store_add_to_basket'),
    path('basket', views.basket, name='store_basket'),
]
