
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from pagina.templates.generales.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import *
from django.core.mail import EmailMessage
from django.conf import settings
from pagina.templates.generales.forms import MetodoPagoForm

# Create your views here.
def inicio(request):
    context={}
    return render(request, 'generales/inicio.html')

def about(request):
    context={}
    return render(request, 'generales/about.html')

def info(request):
    return render(request, 'generales/info.html')

#de acá para abajo se necesita estar log para verles
@login_required
def cursos(request):
    products = Product.objects.all()
    context={'products': products}
    return render(request, 'generales/cursos.html', context)


@login_required
def carrito(request):
    customer=request.user.id
    orden, created= Order.objects.get_or_create(Customer_id=customer, complete=False)
    items= orden.orderitem_set.all()
    context={'items':items, 'order':orden}
    return render(request, 'generales/pagar.html', context)

def exit(request):
    logout(request)
    return redirect('inicio')

def chek(request):
    customer=request.user.id
    orden, created= Order.objects.get_or_create(Customer_id=customer, complete=False)
    items= orden.orderitem_set.all()
    context={'items':items, 'order':orden,'form': MetodoPagoForm()}
    if request.method == 'POST':
        pago_form = MetodoPagoForm(data=request.POST)
        if pago_form.is_valid():
            return redirect('inicio')
    return render(request, 'generales/chek.html', context)

def register(request):
    data = {
        'form': CustomUserCreationForm()
    } 
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            ## LO DEL MAIL
            mail= request.POST.get('email', '')
            email = EmailMessage(
                'Aviso de registro en el sitio web Academia USAC',
                'Usted se ha registrado en el sitio web academia usac por favor esté al tanto de nuestras promociones.',
                settings.EMAIL_HOST_USER,
                [mail],
            )
            email.fail_silently = False
            email.send()
            ## FIN LO DEL MAIL
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('inicio')
    return render(request, 'registration/register.html', data)
        
