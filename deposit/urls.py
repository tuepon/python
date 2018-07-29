from django.urls import path
from . import views

app_name = 'deposit'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'), #/deposit/add
    path('update/<int:pk>/', views.update, name='update')
]