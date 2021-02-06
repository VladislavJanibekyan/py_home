from django.shortcuts import render
import json
def home(request):
	context  = {"name":"Vladislav",
				"surname": "Janibekyan"
				}
	return render(request, "second_app/home.html", context)
def actors(request):
	with open("/Users/vladislav/Desktop/py_home/second_project/second_app/sample_json.json", "r") as file:
		data = json.load(file)
		inside = data["items"]

	
	return render(request, "second_app/actors.html", inside)

# Create your views here.
