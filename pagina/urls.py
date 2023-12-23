from django.urls import path
from . import views
from .views import exit
from .views import register

urlpatterns = [
    path('cursos', views.cursos, name='cursos'),   
    path('about', views.about, name='about'),   
    path('', views.inicio, name='inicio'),    
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('info/', views.info, name='info'),
    path('carrito/', views.carrito, name='carrito'),
]
