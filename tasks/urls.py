from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('addTask/', views.addTask, name='addTask'),
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
    path('updateTask/<int:pk>/', views.updateTask, name='updateTask'),
    path('updateStatusTask/<int:pk>', views.updateStatusTask, name='updateStatusTask'),
]
