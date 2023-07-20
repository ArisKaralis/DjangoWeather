from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests 

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=DC706355-EFE4-4EA6-8BE8-F87749165197")

	try:
		api = json.loads(api_request.text)
	except Exception as e:
		api = "Error..."

	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html', {})  