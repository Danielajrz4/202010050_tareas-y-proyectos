from django.shortcuts import render

# Create your views here.



def inicio(request):
    context={}
    return render(request, 'generales/inicioo.html')

def curso1(request):
    context={}
    return render(request, 'generales/curso1.html')

def pagar(request):
    context={}
    return render(request, 'generales/pagar.html')

def login(request):
    context={}
    return render(request, 'generales/loginn.html')