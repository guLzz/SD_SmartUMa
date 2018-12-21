import urllib.request
import json
import random
import ssl

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
        print("falhou")

#Devolve numero de carros
def parkingAPI():
    try:
        with urllib.request.urlopen("http://84.23.208.186:25000/number_of_cars_parked") as url:
            nr_cars = url.read().decode()

        #print(nr_cars)
        return nr_cars
    except:
        print("falhou")

#Devolve a latencia (pela API) e 2 randoms floats para uplaod e download
def netNtempAPI():
    try:
        with urllib.request.urlopen("https://jpborges.pt/smartuma/api/sensors") as url:
            ping = url.read().decode()

        ping_value = json.loads(ping)

        #json do ping dos ultimos 7 dias
        arrayping = ping_value['data'][1]['average']
        #print(arrayping) #debug do array 
        
        for value in arrayping:
            lag = value
        latencia = abs(int(round(ping_value['data'][1]['average'][lag], 0)))    
        #print(latencia)

        upload = round(random.uniform(20,50), 2) 
        download = round(random.uniform(20,50), 2) 
        #print(upload)
        #print(download)

        #temperaturas das salas
        ##############################################################################
        arraytemps0 = ping_value['data'][3]['average']
        for value in arraytemps0:
            temp = value

        temperatura0 = round(ping_value['data'][3]['average'][temp], 1)
        #print(temperatura0)

        #######
        arraytemps1 = ping_value['data'][5]['average']
        for value in arraytemps1:
            temp = value

        temperatura1 = round(ping_value['data'][5]['average'][temp], 1)
        #print(temperatura1)
        #######
        arraytemps2 = ping_value['data'][9]['average']
        for value in arraytemps2:
            temp = value

        temperatura2 = round(ping_value['data'][9]['average'][temp], 1)
        #print(temperatura2)
        #######
        arraytemps3 = ping_value['data'][7]['average']
        for value in arraytemps3:
            temp = value

        temperatura3 = round(ping_value['data'][7]['average'][temp], 1)
        #print(temperatura3)

        array = [latencia,download,upload,temperatura0,temperatura1,temperatura2,temperatura3]
        return array
    except:
        print("falhou")

def noiseAPI():
    try:
        with urllib.request.urlopen("https://jpborges.pt/smartuma/api/sensors/4/measures") as url:
            ping = url.read().decode()

        ping_value = json.loads(ping)
        #print(ping_value) #debug

        noise0 = abs(int(float(ping_value['data'][3]['value'])))
        #print(noise0)
        #######
        noise1 = abs(int(float(ping_value['data'][5]['value'])))
        #print(noise1)
        #######
        noise2 = abs(int(float(ping_value['data'][9]['value'])))
        #print(noise2)
        #######
        noise3 = abs(int(float(ping_value['data'][7]['value'])))
        #print(noise3)

        array = [noise0,noise1,noise2,noise3]
        return array
    except:
        print("falhou")
#if __name__ == "__main__":
#    parkingAPI()
#    netNtempAPI()
#    studyRoomSeatsAPI()
#    noiseAPI()