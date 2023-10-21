from django.shortcuts import render
import json
import requests


def home(request):
    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=FD6CD5F5-21E5-4E9F-BC67-6A2F7FE03C36")

        # Check the status code to ensure the request was successful
        if api_request.status_code == 200:
            api = json.loads(api_request.content)
        else:
            api = {"error": "API request failed with status code {}".format(
                api_request.status_code)}
    except Exception as e:
        api = {"error": str(e)}

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
