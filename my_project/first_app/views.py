from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

def home(request):
	return HttpResponse("Hello from frist app")
def about(request):
	return HttpResponse("This app is about my first project")
def date(request):
	date  = datetime.now()
	return HttpResponse (date)
def script(request):
	dic = {}
	for i in range(1,16):
		dic[i]= i **2
	return HttpResponse(str(dic))

# Create your views here.
