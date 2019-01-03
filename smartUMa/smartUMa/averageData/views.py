from django.http import HttpResponse
from django.shortcuts import render
from pprint import pprint
from . models import *
import logging

# Create your views here.


def index(request):
    context = {
        'title': 'SmartUMa - History'
    }
    return render(request, 'averageData/index.html', context)


def get_weather():
    weathers = AverageData.objects.only("weather_id", "timestamp")
    data = []
    for average in weathers:
        value = Weather.objects.get(id=average.weather_id)
        data.insert(0, {
            "id": value.id,
            "temperature": value.temperature,
            "humidity": value.humidity,
            "wind_speed": value.wind_speed,
            "wind_direction": value.wind_direction,
            "solar_intensity": value.solar_intensity,
            "timestamp": average.timestamp
        })

    context = {
        "weather": data,
        'title': 'SmartUMa - Weather'
    }

    return context


def weather(request):
    context = get_weather()
    return render(request, 'averageData/weather.html', context)


def details_weather(request):
    context = get_weather()
    return render(request, 'averageData/details_weather.html', context)


def get_parking():
    parks = AverageData.objects.only("parking_id", "timestamp")
    data = []
    for average in parks:
        value = Parking.objects.get(id=average.parking_id)
        data.insert(0, {
            "id": value.id,
            "occupation": value.occupation,
            "timestamp": average.timestamp
        })

    context = {
        "parking": data,
        'title': 'SmartUMa - Parking'
    }

    return context


def parking(request):
    context = get_parking()
    return render(request, 'averageData/parking.html', context)


def details_parking(request):
    context = get_parking()
    return render(request, 'averageData/details_parking.html', context)


def get_network():
    networks = AverageData.objects.only("network_id", "timestamp")
    data = []
    for average in networks:
        value = Network.objects.get(id=average.network_id)
        data.insert(0, {
            "id": value.id,
            "latency": value.latency,
            "download": value.download_speed,
            "upload": value.upload_speed,
            "timestamp": average.timestamp
        }
                    )
    context = {
        "network": data,
        'title': 'SmartUMa - Network'
    }
    return context


def network(request):
    context = get_network()
    return render(request, 'averageData/network.html', context)


def details_network(request):
    context = get_network()
    return render(request, 'averageData/details_network.html', context)


def get_studyroom():
    studyrooms = AverageData.objects.only("studyroom_id", "timestamp")
    data = []
    for average in studyrooms:
        value = StudyRoom.objects.get(id=average.studyroom_id)
        room0 = Floor0.objects.get(id=value.studyroom0_id)
        room1 = Floor1.objects.get(id=value.studyroom1_id)
        room2 = Floor2.objects.get(id=value.studyroom2_id)
        room2pc = Floor2PC.objects.get(id=value.studyroom2PC_id)
        room3 = Floor3.objects.get(id=value.studyroom3_id)
        data.insert(0, {
            "id": value.id,
            "room0": room0,
            "room1": room1,
            "room2": room2,
            "room2PC": room2pc,
            "room3": room3,
            "timestamp": average.timestamp
        }
                    )

    context = {
        "studyroom": data,
        'title': 'SmartUMa - Study Rooms'
    }

    return context


def studyroom(request):
    context = get_studyroom()
    return render(request, 'averageData/studyroom.html', context)


def details_studyroom(request):
    context = get_studyroom()
    return render(request, 'averageData/details_studyroom.html', context)
