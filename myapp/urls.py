from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index , name='index'),
    path('', views.index , name = 'index1'),
    path('create', views.createTask , name='createTask'),
    path('submit',views.submit,name='submit'),
]