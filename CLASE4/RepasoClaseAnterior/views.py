from django.shortcuts import render

# Create your views here.


def FirstView(request):
    return render(
        request,
        'RepasoClaseAnterior/index.html',
        {'Nombre': 'Juan'}
    )

def SecondtView(request, name):
    return render(
        request,
        'RepasoClaseAnterior/index.html',
        {'Nombre': name}
    )
