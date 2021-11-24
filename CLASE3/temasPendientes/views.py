from django.shortcuts import render, redirect
from . import forms

# Create your views here.


def index(request):
    return render(
        request,
        'temasPendientes/index.html'
    )


""" 
Ejercicio 1
Crear 2 vistas con sus propios templates con los nombres;
- Contact
- Abous us
3 min 10.50
"""


def nosotros(request):
    return render(
        request,
        'temasPendientes/nosotros.html',
    )


def contacto(request):
    # Creo una instancia de mi formulario
    form = forms.FormularioDeContacto()

    if request.method == "POST":
        form = forms.FormularioDeContacto(request.POST)
        print(form)
        if form.is_valid():
            return redirect('index')
        else:
            return render(
                request,
                'temasPendientes/contacto.html',
                {'form': form, 'errpr': 'hay un error'}
            )

    return render(
        request,
        'temasPendientes/contacto.html',
        {'form': form}
    )


def quejas(request):
    form = forms.FormularioDeQuejas()
    

    # Si es un POST
    if request.method == 'POST':
        # Me saque la información del mensaje
        form = forms.FormularioDeQuejas(request.POST)
        # Valido que la información llegada cumple con lo descripto en forms.py
        if form.is_valid():
            print("Todo ok")

    return render(
        request,
        'temasPendientes/quejas.html',
        {'form': form}
    )

    """ 
    Ejericicio 3
    Crear un vista con formulario y html propio que sea para hacer un login.

    charField
    charPassowrd

    4min 12.44AM

    """

def login(request):
    form = forms.FormularioLogin()

    if request.method == 'POST':
        form = forms.FormularioLogin(request.POST)
        if form.is_valid():
            return redirect('index')

    return render(
        request,
        'temasPendientes/login.html',
        {"form" : form}
    )