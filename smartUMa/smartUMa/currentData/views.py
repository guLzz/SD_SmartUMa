from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps
# Create your views here.


def index(request):
    model_parking = apps.get_model('parking', 'Parking')
    model_weather = apps.get_model('weather', 'Weather')
    model_studyroom = apps.get_model('studyroom', 'StudyRoom')
    model_network = apps.get_model('network', 'Network')

    parking = model_parking.objects.latest('timestamp')
    weather = model_weather.objects.latest('timestamp')
    studyroom0 = model_studyroom.objects.filter(room='0').latest('timestamp')
    studyroom1 = model_studyroom.objects.filter(room='1').latest('timestamp')
    studyroom2 = model_studyroom.objects.filter(room='2').latest('timestamp')
    studyroom2_pc = model_studyroom.objects.filter(room='2-PC').latest('timestamp')
    studyroom3 = model_studyroom.objects.filter(room='3').latest('timestamp')
    network = model_network.objects.latest('timestamp')

    context = {
        'title': 'SmartUMa - Current State',
        'parking': parking,
        'weather': weather,
        'studyroom0': studyroom0,
        'studyroom1': studyroom1,
        'studyroom2': studyroom2,
        'studyroom2PC': studyroom2_pc,
        'studyroom3': studyroom3,
        'network': network,
    }

    return render(request, 'currentData/index.html', context)
