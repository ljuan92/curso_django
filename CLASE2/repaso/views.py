from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def VistaSimple(request):
    return HttpResponse("Hola")


def Saludar(request, name):
    return HttpResponse("Hola, " + name.capitalize() + " como estas?")


def DatosPersona(request, name, lastName, age):
    return HttpResponse(name.capitalize() + " " + lastName.capitalize() + " tiene " + age + " años ")


def UsoDelHtmlConMalasPracticas(request):
    return HttpResponse("""
            <h1> Titulo</h1>
            <p> Este es un parrafo</p>
    """)


def usoCorrectoDeUnHtml(request):
    return render(request, 'repaso/index.html')


def CargarHtmlConContexto(request):
    # return render(request, 'carpeta_nombre_app/template.html', context={ es un diccionario !!!})
    return render(request, 'repaso/indexConContexto.html', {
        "name": "Matias",
        "lastName": "Rapa",
        "status": "demorado",
        "Pendientes": ['comprar tomate', 'lavar la ropa', 'sacar al perro', 'estudiar Django']
    })

def emocion(request, name, lastName, emocion    ):
    return render(request, 'repaso/indexemocion.html', {
        "name": "Juan",
        "lastName": "Lago",
        "emocion": "Enojado"
    })

lista = [
    {"name":"tomate", "status": "ok"},
    {"name":"Cocacola", "status": "nook"},
    {"name":"Lechuga", "status": "ok"},
    {"name":"Manzana", "status": "ok"}
    ]

def ejercicio4(request):
    return render(
        request,
        'repaso/ejercicio4.html',
        {"lista": lista}
    )
