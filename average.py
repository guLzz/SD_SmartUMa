import time
import pymysql.cursors

from contextlib import closing
from datetime import datetime, timedelta

def getValuesWeather():
    try:
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="smartUMa"
            )

        with closing( mydb.cursor() ) as mycursor:
            mycursor = mydb.cursor()

            tim = datetime.now()
            actualTime = ('{:%Y-%m-%d %H:%M:%S}'.format(tim))
            dayB4 = tim - timedelta(1)
            dayBefore = ('{:%Y-%m-%d %H:%M:%S}'.format(dayB4))

            #print(actualTime)
            #print(dayBefore)
            
            ## temperature ##
            sql = "SELECT temperature FROM weather_weather WHERE timestamp BETWEEN '"+ str(dayBefore) +"' AND '"+ str(actualTime) +"'"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            #print(myresult)
            #print(len(myresult))
            
            medTemp = 0

            for x in myresult :
                medTemp = medTemp + x[0]

            medTemp = round(medTemp / len(myresult),1) 
            #print(medTemp)

            ## humidity ##
            sql = "SELECT humidity FROM weather_weather WHERE timestamp BETWEEN '"+ str(dayBefore) +"' AND '"+ str(actualTime) +"'"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            #print(myresult)
            #print(len(myresult))
            
            medHum = 0

            for x in myresult :
                medHum = medHum + x[0]

            medHum = round(medHum / len(myresult),1) 
            #print(medHum)

            ## wind_speed ##
            sql = "SELECT wind_speed FROM weather_weather WHERE timestamp BETWEEN '"+ str(dayBefore) +"' AND '"+ str(actualTime) +"'"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            #print(myresult)
            #print(len(myresult))
            
            medWS = 0

            for x in myresult :
                medTemp = medWS + x[0]

            medWS = round(medWS / len(myresult),1) 
            #print(medWS)

            ## wind_direction ##
            sql = "SELECT wind_direction FROM weather_weather WHERE timestamp BETWEEN '"+ str(dayBefore) +"' AND '"+ str(actualTime) +"'"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            #print(myresult)
            #print(len(myresult))
            
            medWD = averageWind(myresult)
            
            ## solar_intensity ##
            sql = "SELECT solar_intensity FROM weather_weather WHERE timestamp BETWEEN '"+ str(dayBefore) +"' AND '"+ str(actualTime) +"'"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            #print(myresult)
            #print(len(myresult))
            
            medSol = 0

            for x in myresult :
                medSol = medSol + x[0]

            medSol = round(medSol / len(myresult),1) 
            #print(medSol)

        mydb.close()
        array = [medTemp,medHum,medWS,medWD,medSol]
        return array

    except:
        print("failed average weather")

def averageWind(result):
    
    windD = []

    for x in result:
        windD.append(x[0])

    windDirection = max(set(windD), key=windD.count)
    
    #print(windDirection)
    return windDirection

def getValuesParking():
    try:
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="smartUMa"
            )

        with closing( mydb.cursor() ) as mycursor:
            mycursor = mydb.cursor()

            tim = datetime.now()
            actualTime = ('{:%Y-%m-%d %H:%M:%S}'.format(tim))
            dayB4 = tim - timedelta(1)
            dayBefore = ('{:%Y-%m-%d %H:%M:%S}'.format(dayB4))

            sql = "SELECT occupation FROM parking_parking WHERE timestamp BETWEEN '"+ str(dayBefore) +"' AND '"+ str(actualTime) +"'"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            #print(myresult)
            
            medCars = 0

            for x in myresult :
                medCars = medCars + x[0]

            medCars = int(round(medCars / len(myresult),0)) 
        
        mydb.close()
        #print(medCars)
        return medCars
    except:
        print("failed: average parking")

def getValuesNetwork():
    try:
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="smartUMa"
            )

        with closing( mydb.cursor() ) as mycursor:
            mycursor = mydb.cursor()

            tim = datetime.now()
            actualTime = ('{:%Y-%m-%d %H:%M:%S}'.format(tim))
            dayB4 = tim - timedelta(1)
            dayBefore = ('{:%Y-%m-%d %H:%M:%S}'.format(dayB4))

            ##latencia##
            sql = "SELECT latency FROM network_network WHERE timestamp BETWEEN '"+ str(dayBefore) +"' AND '"+ str(actualTime) +"'"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            #print(myresult)
            
            
            medLag = 0

            for x in myresult :
                medLag = medLag + x[0]

            medLag = int(round(medLag / len(myresult),0)) 

            ##download##
            sql = "SELECT download_speed FROM network_network WHERE timestamp BETWEEN '"+ str(dayBefore) +"' AND '"+ str(actualTime) +"'"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            #print(myresult)
            
            
            medDownload = 0

            for x in myresult :
                medDownload = medDownload + x[0]

            medDownload = round(medDownload / len(myresult),1) 

            ##upload##
            sql = "SELECT upload_speed FROM network_network WHERE timestamp BETWEEN '"+ str(dayBefore) +"' AND '"+ str(actualTime) +"'"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            #print(myresult)
            
            
            medUpload = 0

            for x in myresult :
                medUpload = medUpload + x[0]

            medUpload = round(medUpload / len(myresult),1)
            
        
        mydb.close()
        #print(medLag)
        #print(medDownload)
        #print(medUpload)
        array = [medLag, medDownload, medUpload]
        return array
    except:
        print("failed: average network")

#tendo em conta que os valores do 2-PC sao uma copia do 2 entao na chamada chamar 2 e na insercao inserir como 2-PC
def getValuesStudyRoom(sala):
    try:
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="smartUMa"
            )

        with closing( mydb.cursor() ) as mycursor:
            mycursor = mydb.cursor()

            tim = datetime.now()
            actualTime = ('{:%Y-%m-%d %H:%M:%S}'.format(tim))
            dayB4 = tim - timedelta(1)
            dayBefore = ('{:%Y-%m-%d %H:%M:%S}'.format(dayB4))

            ##temperature##
            sql = "SELECT temperature FROM studyroom_studyroom WHERE room LIKE "+sala+" AND timestamp BETWEEN '"+ str(dayBefore) +"' AND '"+ str(actualTime) +"'"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            #print(myresult)
            
            medTemp = 0

            for x in myresult :
                medTemp = medTemp + x[0]

            medTemp = round(medTemp / len(myresult),1)

            ##occupation##
            sql = "SELECT occupation FROM studyroom_studyroom WHERE room LIKE "+sala+" AND timestamp BETWEEN '"+ str(dayBefore) +"' AND '"+ str(actualTime) +"'"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            #print(myresult)
            
            medOccupation = 0

            for x in myresult :
                medOccupation = medOccupation + x[0]

            medOccupation = int(round(medOccupation / len(myresult),0))

            ##noise##
            sql = "SELECT noise FROM studyroom_studyroom WHERE room LIKE "+sala+" AND timestamp BETWEEN '"+ str(dayBefore) +"' AND '"+ str(actualTime) +"'"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            #print(myresult)
            
            medNoise = 0

            for x in myresult :
                medNoise = medNoise + x[0]

            medNoise = int(round(medNoise / len(myresult),0))


        mydb.close()
        #print(medTemp)
        #print(medOccupation)
        #print(medNoise)
        array = [medTemp, medOccupation, medNoise]
        return array


    except:
        print("failed: average study room values")

def averageStudyroomIDs(): 
    try:
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="smartUMa"
            )

        with closing( mydb.cursor() ) as mycursor:
            mycursor = mydb.cursor()
            
            ##floor 0
            sql = "SELECT id FROM averagedata_floor0"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()
            #print(myresult)
            
            id_F0 = max(myresult)
            #print(id_F0[0])

            ##floor 1
            sql = "SELECT id FROM averagedata_floor1"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()
            #print(myresult)
            
            id_F1 = max(myresult)
            #print(id_F1[0])
            
            ##floor 2
            sql = "SELECT id FROM averagedata_floor2"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()
            #print(myresult)
            
            id_F2 = max(myresult)
            #print(id_F2[0])

            ##floor 2-PC
            sql = "SELECT id FROM averagedata_floor2pc"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()
            #print(myresult)
            
            id_F2PC = max(myresult)
            #print(id_F2PC[0])

            ##floor 3
            sql = "SELECT id FROM averagedata_floor3"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()
            #print(myresult)
            
            id_F3 = max(myresult)
            #print(id_F3[0])

            average_ids = [id_F0[0], id_F1[0], id_F2[0], id_F2PC[0], id_F3[0]]
            #print(average_ids)

        mydb.close()

        return average_ids

    except:
        print("failed: average study room ids")

def averageDataIDs():
    try:
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="smartuma"
            )

        with closing( mydb.cursor() ) as mycursor:
            mycursor = mydb.cursor()
            
            ##Network
            sql = "SELECT id FROM averagedata_network"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()
            #print(myresult)
            
            id_Network = max(myresult)
            #print(id_Network[0])

            ##Parking
            sql = "SELECT id FROM averagedata_parking"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()
            #print(myresult)
            
            id_Parking = max(myresult)
            #print(id_Parking[0])
            
            ##Studyrooms
            sql = "SELECT id FROM averagedata_studyroom"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()
            #print(myresult)
            
            id_Studyroom = max(myresult)
            #print(id_Studyroom[0])

            ##Weather
            sql = "SELECT id FROM averagedata_weather"
            mycursor.execute(sql)

            myresult = mycursor.fetchall()
            #print(myresult)
            
            id_Weather = max(myresult)
            #print(id_Weather[0])

            average_ids = [id_Network[0], id_Parking[0], id_Studyroom[0], id_Weather[0]]
            #print(average_ids)

        mydb.close()

        return average_ids

    except:
        print("failed: average data ids")



#if __name__ == "__main__":
#    averageDataIDs()
#    averageStudyroom()
#    getValuesWeather()
#    getValuesParking()    
#    getValuesNetwork()
#    getValuesStudyRoom("2")