from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='loginn'),
    path('pagar/', views.pagar, name='pagar'),
    path('inicio/', views.inicio, name='inicio'),
    path('curso1', views.curso1, name='curso1'),
]