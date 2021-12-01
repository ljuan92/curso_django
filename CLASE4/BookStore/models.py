from django.db import models

# Create your models here.


class Book(models.Model):
    # CharField es texto corto en base de datos.
    title = models.CharField(max_length=60)
    # Por ahora lo dejamos como texto despues vemos como trabajar con fechas
    year = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    synopsis = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    editorial = models.CharField(max_length=60)
    stock = models.IntegerField(default=0)
