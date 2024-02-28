from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='food_diary_index'),
    path('delete/<entry_id>', views.delete_entry, name='food_diary_delete_entry'),
]
