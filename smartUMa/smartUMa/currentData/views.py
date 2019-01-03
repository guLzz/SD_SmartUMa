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


def details_weather(request):
    model_weather = apps.get_model('weather', 'Weather')
    weather = model_weather.objects.latest('timestamp')
    context = {
        'title': 'SmartUMa - Current State',
        'weather': weather
    }
    return render(request, 'currentData/weather.html', context)


def details_parking(request):
    model_parking = apps.get_model('parking', 'Parking')

    parking = model_parking.objects.latest('timestamp')

    context = {
        'title': 'SmartUMa - Current State',
        'parking': parking
    }
    return render(request, 'currentData/parking.html', context)


def details_network(request):
    model_network = apps.get_model('network', 'Network')
    network = model_network.objects.latest('timestamp')

    context = {
        'title': 'SmartUMa - Current State',
        'network': network,
    }
    return render(request, 'currentData/network.html', context)


def details_studyroom(request):
    model_studyroom = apps.get_model('studyroom', 'StudyRoom')
    studyroom0 = model_studyroom.objects.filter(room='0').latest('timestamp')
    studyroom1 = model_studyroom.objects.filter(room='1').latest('timestamp')
    studyroom2 = model_studyroom.objects.filter(room='2').latest('timestamp')
    studyroom2_pc = model_studyroom.objects.filter(room='2-PC').latest('timestamp')
    studyroom3 = model_studyroom.objects.filter(room='3').latest('timestamp')

    context = {
        'title': 'SmartUMa - Current State',
        'studyroom0': studyroom0,
        'studyroom1': studyroom1,
        'studyroom2': studyroom2,
        'studyroom2PC': studyroom2_pc,
        'studyroom3': studyroom3,
    }
    return render(request, 'currentData/studyroom.html', context)


def average_studyroom(my_room):
    model_studyroom = apps.get_model('studyroom', 'StudyRoom')
    studyroom = model_studyroom.objects.filter(room=my_room).all()
    reference = model_studyroom.objects.filter(room=my_room).earliest('timestamp')

    num = 0
    total_temperature = 0
    total_occupation = 0
    total_noise = 0

    for state in studyroom:
        num += 1
        total_temperature += state.temperature
        total_occupation += state.occupation
        total_noise += state.noise

    data = {
        'sampleNumber': num,
        'time': reference.timestamp,
        'room': reference.room,
        'averageTemperature': int(round(total_temperature / num)),
        'averageOccupation': int(round(total_occupation / num)),
        'averageNoise': int(round(total_noise / num))
    }

    return data


def average_parking():
    model_parking = apps.get_model('parking', 'Parking')

    parking = model_parking.objects.all()
    reference = model_parking.objects.earliest('timestamp')

    num = 0
    total = 0
    for state in parking:
        num += 1
        total += state.occupation

    data = {
        'sampleNumber': num,
        'time': reference.timestamp,
        'averageOccupation': int(round(total/num))
    }

    return data


def average_network():
    model_network = apps.get_model('network', 'Network')

    network = model_network.objects.all()
    reference = model_network.objects.earliest('timestamp')

    num = 0
    total_latency = 0
    total_download = 0
    total_upload = 0

    for state in network:
        num += 1
        total_latency += state.latency
        total_download += state.download_speed
        total_upload += state.upload_speed

    data = {
        'sampleNumber': num,
        'time': reference.timestamp,
        'averageLatency': int(round(total_latency/num)),
        'averageDownload': int(round(total_download/num)),
        'averageUpload': int(round(total_upload/num))
    }

    return data


def average_weather():
    model_weather = apps.get_model('weather', 'Weather')
    # model_studyroom = apps.get_model('studyroom', 'StudyRoom')

    weather = model_weather.objects.all()
    reference = model_weather.objects.earliest('timestamp')

    num = 0
    total_temperature = 0
    total_humidity = 0
    total_wind_speed = 0
    total_solar_intensity = 0

    for state in weather:
        num += 1
        total_temperature += state.temperature
        total_humidity += state.humidity
        total_wind_speed += state.wind_speed
        total_solar_intensity += state.solar_intensity

    data = {
        'sampleNumber': num,
        'time': reference.timestamp,
        'averageTemperature': int(round(total_temperature/num)),
        'averageHumidity': int(round(total_humidity/num)),
        'averageWindSpeed': int(round(total_wind_speed/num)),
        'averageSolarIntensity': int(round(total_solar_intensity/num))
    }

    return data
