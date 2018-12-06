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


def weather(request):
    weathers = AverageData.objects.only("weather_id", "timestamp")
    data = []
    for average in weathers:
        value = Weather.objects.get(id=average.weather_id)
        data.insert(0, {
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

    return render(request, 'averageData/weather.html', context)


def parking(request):
    parks = AverageData.objects.only("parking_id", "timestamp")
    data = []
    for average in parks:
        value = Parking.objects.get(id=average.parking_id)
        data.insert(0, {
            "occupation": value.occupation,
            "timestamp": average.timestamp
        })

    context = {
        "parking": data,
        'title': 'SmartUMa - Parking'
    }

    return render(request, 'averageData/parking.html', context)


def network(request):
    networks = AverageData.objects.only("network_id", "timestamp")
    data = []
    for average in networks:
        value = Network.objects.get(id=average.network_id)
        data.insert(0, {
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
    logger = logging.getLogger(__name__)
    logger.debug(data)
    return render(request, 'averageData/network.html', context)


def studyroom(request):
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
    return render(request, 'averageData/studyroom.html', context)
