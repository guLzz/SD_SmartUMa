from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather, name="weather"),
    path('parking/', views.parking, name="parking"),
    path('network/', views.network, name="network"),
    path('studyroom/', views.studyroom, name="studyroom"),
    path('', views.index, name="index")
]
