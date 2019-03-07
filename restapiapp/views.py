from rest_framework.views import APIView
from rest_framework.response import Response
import json
from urllib.request import urlopen
""" Python HTTP library,to make HTTP requests simpler and more human-friendly """
import requests


class TemperatureFahrenheit(APIView):
    """
    Get Temperature of current location using Class Base Rest full Api.

    Restful Api URL: http://localhost:8000/temperature/fahrenheit
    
    """

    def get(self, request):
        """ This will get user IP wise location """

        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        city = data['city']

        """ http://api.openweathermap.org online service that provides weather data """
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=dfc4877f0ed4f8aa5bc3f182855d856f&q='

        """ join api and city with fahrenheit unit """
        url = api_address + city + '&units=imperial'

        """ get response in json format of city temperature """
        json_data = requests.get(url).json()

        """ get city temp in fahrenheit """
        fahrenheit = json_data['main']['temp']

        return Response(city + ' location temperature in fahrenheit is: ' + str(fahrenheit) + str(json_data))

