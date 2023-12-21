from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from pagina.templates.generales.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login



# Create your views here.
def inicio(request):
    context={}
    return render(request, 'generales/inicio.html')

def about(request):
    context={}
    return render(request, 'generales/about.html')

#de acá para abajo se necesita estar log para verles
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

def register(request):
    data = {
        'form': CustomUserCreationForm()
    } 
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)

            return redirect('inicio')
        
    return render(request, 'registration/register.html', data)

