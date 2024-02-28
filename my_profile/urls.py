from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='my_profile_index'),
    path('delete/<entry_id>', views.delete_food_diary_entry, name='my_profile_delete_food_diary_entry'),
]
