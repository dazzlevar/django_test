from django.shortcuts import render #Funciones para pintar el html
from django.http import HttpResponse #Funciones para trabajar con html
from django.template import loader #Funciones para cargar con html
from weather.models import Weather #Se carga la tabla weather de la base de datos
from weather.forms import WeatherForm #Se esta cargando un formulario WeatherForm

#Tarea: crear y retornar una tabla html

def home(request): #
    form= WeatherForm(request.POST or None)
    if form.is_valid():
        form.save()
    weathers = Weather.objects.all()
    context = {
        'weather_list': weathers,
        'form': form
    }
    return render(request, 'weather/index.html', context)


