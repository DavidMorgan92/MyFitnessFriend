from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='my_profile_index'),
    path('orders', views.orders, name='my_profile_orders'),
]
