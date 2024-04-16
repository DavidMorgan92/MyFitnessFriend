from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='goals_index'),
    path('wizard', views.wizard, name='goals_wizard'),
]
