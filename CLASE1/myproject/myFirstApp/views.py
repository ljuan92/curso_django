from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Saludar(request):
    return HttpResponse("Hola, como estas?")

def Enojado(request):
    return HttpResponse("<h1 style='text-align: center;'>Estoy enojado</h1>")

def Feliz(request):
    return HttpResponse("<h1 style='text-align: center;'>Estoy feliz</h1>")

def Triste(request):
    return HttpResponse("<h1 style='text-align: center;'>Estoy triste</h1>")