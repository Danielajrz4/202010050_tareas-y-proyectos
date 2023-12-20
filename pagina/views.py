from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def inicio(request):
    context={}
    return render(request, 'generales/inicio.html')

def login(request):
    context={}
    return render(request, 'generales/loginnn.html')

def registro(request):
    context={}
    return render(request, 'generales/registro.html')


@login_required
def cursos(request):
    context={}
    return render(request, 'generales/cursos.html')

def curso1(request):
    context={}
    return render(request, 'generales/curso1.html')

def pagar(request):
    context={}
    return render(request, 'generales/pagar.html')

def exit(request):
    logout(request)
    return redirect('inicio')


