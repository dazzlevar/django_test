from django.shortcuts import render #Funciones para pintar el html
from django.http import HttpResponse #Funciones para trabajar con html
from django.template import loader #Funciones para cargar con html

def home(request):
    context = {}
    return render(request, 'calculadora.html', context)


    