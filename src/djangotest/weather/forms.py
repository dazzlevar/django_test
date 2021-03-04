from django import forms
from weather.models import Weather

class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields= ["country_name", "grades"]
