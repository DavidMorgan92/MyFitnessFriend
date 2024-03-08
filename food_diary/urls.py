from django.urls import path, register_converter
from . import views, converters

register_converter(converters.DateConverter, 'date')

urlpatterns = [
    path('', views.index, name='food_diary_index'),
    path('delete/<int:entry_id>', views.delete_entry,
         name='food_diary_delete_entry'),
    path('add/<date:date>', views.add_entry, name='food_diary_add_entry'),
]
