from django.urls import path
from . import views
from .views import exit
from .views import register

urlpatterns = [
    path('pagar', views.pagar, name='pagar'),  
    path('cursos', views.cursos, name='cursos'),  
    path('curso1', views.curso1, name='curso1'),  
    path('about', views.about, name='about'),   
    path('', views.inicio, name='inicio'),    
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
]
