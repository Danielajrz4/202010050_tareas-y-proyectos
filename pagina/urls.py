from django.urls import path
from . import views
from .views import exit
urlpatterns = [
    path('login', views.login, name='login'),  
    path('pagar', views.pagar, name='pagar'),  
    path('cursos', views.cursos, name='cursos'),  
    path('curso1', views.curso1, name='curso1'),  
    path('registro', views.registro, name='registro'),   
    path('', views.inicio, name='inicio'),    
    path('logout/', exit, name='exit'),
]
