from django.urls import path
from . import views

urlpatterns = [
    path('my_todo/', views.index, name='index'),
]
