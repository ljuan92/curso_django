# curso_django


## Clase 4

1. Crear Proyecto

2. Crear app ``python manage.py startapp RepasoClaseAnterior``

3. Agregar ``include`` a ``urls.py``

4. Agregar ``RepasoClaseAnterior`` a ``urlpatterns``

5. incluir ``path('repaso/', include('RepasoClaseAnterior.urls'))`` en 'urlpatterns' del proyecto.

6. Crear urls.py en la carpeta de la app e incertar la estructura

7. Crear templates/RepasoClaseAnterior/index.html

8. En el archivo urls.py de la app se importa views habiendo hecho el paso numero 5 y se incluye en urlpatterns:

|   ``urlpatterns = [
|       path('', views.FirstView)
|   ]``

## Crear vista (Ejemplo)

|   ``def FirstView(request):
|       return render(
|           request,
|           'RepasoClaseAnterior/index.html',
|           {}
|       )``