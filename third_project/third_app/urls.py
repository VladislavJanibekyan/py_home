from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home_page"),
    path("third_project/third_app/templates/third_app/films.html", views.films, name = "films"),
]

#Ստեղծում ենք film անունով table պահում ենք էնտեղ տվյալներ, ու համապատասխան
#url-ի միջոցով ցույց ենք տալիս բոլոր ֆիլմերը, ֆիլմերը պետք ա երևան admin պանելից նույնպես