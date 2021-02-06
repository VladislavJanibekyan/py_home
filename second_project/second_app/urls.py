from django.urls import path
from . import views

urlpatterns = [
		path("", views.home, name = "home"),
		path("second_project/second_app/templates/second_app/actors.html", views.actors, name="actor")
	
]