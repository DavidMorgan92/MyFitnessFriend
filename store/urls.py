from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='store_index'),
    path('search', views.search, name='store_search'),
    path('details/<int:id>', views.details, name='store_details'),
]
