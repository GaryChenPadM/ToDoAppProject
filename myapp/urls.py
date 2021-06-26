from django.urls import path
from . import views

urlpatterns = [
    path('create', views.index , name='create'),
    path('index', views.toDoList , name = 'todoList'),
    path('todoList', views.toDoList , name='todoList'),
    path('submit',views.submit,name='submit'),
]