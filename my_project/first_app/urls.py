from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("about", views.about, name="about_us"),
    path("date", views.date, name="date"),
    path("script", views.script, name="script"),
]