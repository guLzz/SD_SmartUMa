from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather, name="weather"),
    path('parking/', views.parking, name="parking"),
    path('network/', views.network, name="network"),
    path('studyroom/', views.studyroom, name="studyroom"),
    path('', views.index, name="index"),
    path('details/parking/', views.details_parking, name="parking"),
    path('details/network/', views.details_network, name="network"),
    path('details/weather/', views.details_weather, name="weather"),
    path('details/studyroom/', views.details_studyroom, name="studyroom"),
]
