from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='my_profile_index'),
]
