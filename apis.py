import urllib.request
import json
import random
import ssl

from datetime import datetime
from ModuloDB import get_num

#Devolve numero de carros
def studyRoomSeatsAPI():
    try:
        context = ssl._create_unverified_context()
        with urllib.request.urlopen("https://smartrooms.ddns.net/api/rooms/occupation" , context=context) as url:
            seatsarray = url.read().decode()

        seatsinfo = json.loads(seatsarray)
        #print(seatsinfo)
        piso0 = seatsinfo[0]
        piso1 = seatsinfo[1]
        piso2 = seatsinfo[2]
        piso3 = seatsinfo[3]

        piso0ocupation = piso0['occupied_seats']
        #print(piso0ocupation)
        piso1ocupation = piso1['occupied_seats']
        #print(piso1ocupation)
        piso2ocupation = piso2['occupied_seats']
        #print(piso2ocupation)
        piso3ocupation = piso3['occupied_seats']
        #print(piso3ocupation)

        array = [piso0ocupation,piso1ocupation,piso2ocupation,piso3ocupation]
        return array
    except:
        print("failed: ocupation")

#Devolve numero de carros
def parkingAPI():
    try:
        with urllib.request.urlopen("http://84.23.208.186:25000/number_of_cars_parked") as url:
            nr_cars = url.read().decode()

        #print(nr_cars)
        return nr_cars
    except:
        print("failed: parking")

#Devolve a latencia (pela API) e 2 randoms floats para uplaod e download#
def netNtempAPI():
    try:
        with urllib.request.urlopen("https://jpborges.pt/smartuma/api/sensors") as url:
            ping = url.read().decode()

        ping_value = json.loads(ping)
        
        #json do ping dos ultimos 7 dias
        arrayping = ping_value['data'][1]['average']
        #print(arrayping) #debug do array 
        
        lag = max(arrayping)
        
        #print(str(ping_value['data'][1]['average'][lag]))
        latencia = abs(int(round(ping_value['data'][1]['average'][lag], 0)))    
        #print(latencia)

        upload = round(random.uniform(20,50), 2) 
        download = round(random.uniform(20,50), 2) 
        #print(upload)
        #print(download)

        #temperaturas das salas
        ##############################################################################
        arraytemps0 = ping_value['data'][3]['average']
        
        temp = max(arraytemps0)

        temperatura0 = round(ping_value['data'][3]['average'][temp], 1)
        #print(temperatura0)

        #######
        arraytemps1 = ping_value['data'][5]['average']
        
        temp = max(arraytemps1)

        temperatura1 = round(ping_value['data'][5]['average'][temp], 1)
        #print(temperatura1)
        #######
        arraytemps2 = ping_value['data'][9]['average']
        
        temp = max(arraytemps2)

        temperatura2 = round(ping_value['data'][9]['average'][temp], 1)
        #print(temperatura2)
        #######
        arraytemps3 = ping_value['data'][7]['average']
        
        temp = max(arraytemps3)

        temperatura3 = round(ping_value['data'][7]['average'][temp], 1)
        #print(temperatura3)

        array = [latencia,download,upload,temperatura0,temperatura1,temperatura2,temperatura3]
        return array
    except:
        print("failed: network and temperatures(rooms)")

def noiseAPI():
    try:
        with urllib.request.urlopen("http://checkstudynoise.ddns.net/wp-json/sound/sala-estudo-0") as url:
            sound = url.read().decode()
        
        sound_value = json.loads(sound)
        #print(sound_value) #debug
        max_value = len(sound_value) - 1
        noise0 = sound_value[max_value]['value']
        #print(noise0)

        with urllib.request.urlopen("http://checkstudynoise.ddns.net/wp-json/sound/sala-estudo-1") as url:
            sound1 = url.read().decode()
        
        sound_value1 = json.loads(sound1)
        #print(sound_value) #debug
        max_value1 = len(sound_value1) - 1
        noise1 = sound_value1[max_value1]['value']
        #print(noise1)
        
        with urllib.request.urlopen("http://checkstudynoise.ddns.net/wp-json/sound/nucleo-informatica-1") as url:
            sound2 = url.read().decode()
        
        sound_value2 = json.loads(sound2)
        #print(sound_value) #debug
        max_value2 = len(sound_value2) - 1
        noise2 = sound_value2[max_value2]['value']
        #print(noise2)
        
        with urllib.request.urlopen("http://checkstudynoise.ddns.net/wp-json/sound/sala-estudo-3") as url:
            sound3 = url.read().decode()
        
        sound_value3 = json.loads(sound3)
        #print(sound_value) #debug
        max_value3 = len(sound_value3) - 1
        noise3 = sound_value3[max_value3]['value']
        #print(noise3)

        array = [noise0,noise1,noise2,noise3]
        return array
        
    except:
        print("failed: noise (room)")



#if __name__ == "__main__":
#    parkingAPI()
#    netNtempAPI()
#    studyRoomSeatsAPI()
#    noiseAPI()