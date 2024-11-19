import urllib.request
import json
from django.shortcuts import render

def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        url = f'http://api.weatherapi.com/v1/current.json?key=fa3006578482448a9ff143043241911&q={city}&aqi=no'

        try:
            source = urllib.request.urlopen(url).read()
            list_of_data = json.loads(source)
            
            data = {
                "country": list_of_data['location']['country'],
                "city": list_of_data['location']['name'],
                "region": list_of_data['location']['region'],
                "temp": str(list_of_data['current']['temp_c']) + ' °C',
                "condition": list_of_data['current']['condition']['text'],
                "icon": list_of_data['current']['condition']['icon'],
                "wind_kph": str(list_of_data['current']['wind_kph']) + ' kph',
                "humidity": str(list_of_data['current']['humidity']) + '%',
            }
            
            return render(request, "main/index.html", {"data": data})
        except Exception as e:
            data = {"error": "Could not retrieve weather data. Please try again."}
            print(f"Error: {e}")
    else:
        data = {}

    return render(request, "main/index.html")
