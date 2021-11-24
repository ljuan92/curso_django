from django.contrib import admin
from django.urls import path
from .views import VistaSimple, Saludar, DatosPersona, UsoDelHtmlConMalasPracticas, usoCorrectoDeUnHtml, CargarHtmlConContexto, emocion, ejercicio4


urlpatterns = [
    path('vista/', VistaSimple),
    path('hola/<str:name>', Saludar),
    path('datos/<str:name>/<str:lastName>/<str:age>', DatosPersona),
    path('malaPractica/', UsoDelHtmlConMalasPracticas),
    path('buenaPractica/', usoCorrectoDeUnHtml),
    path('htmlconcontexto/', CargarHtmlConContexto),
    path('emocion/', emocion),
    path('ejercicio4/', ejercicio4)


]