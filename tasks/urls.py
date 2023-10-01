from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('addTask/', views.addTask, name='addTask'),
    path('deleteTask/', views.deleteTask, name='deleteTask'),
]
