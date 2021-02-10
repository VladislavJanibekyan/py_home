from django.shortcuts import render
from .models import Film

# Create your views here.
def home(request):
    return render(request, "third_app/home.html")

def films(request):
    item = Film.objects.all()
    context = {
        "item" : item
    }
    return render(request, "third_app/films.html", context)