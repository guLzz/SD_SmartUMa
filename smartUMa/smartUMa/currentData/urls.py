from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('details/weather', views.details_weather, name="weather"),
    path('details/parking', views.details_parking, name="parking"),
    path('details/network', views.details_network, name="network"),
    path('details/studyroom', views.details_studyroom, name="studyroom")
]
