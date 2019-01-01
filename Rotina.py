import time
import pymysql.cursors
import socket

from threading import *
from contextlib import closing
from datetime import datetime
from ModuloDB import convertToValue
from apis import parkingAPI,netNtempAPI,studyRoomSeatsAPI,noiseAPI
from average import getValuesWeather, getValuesNetwork, getValuesParking, getValuesStudyRoom, averageStudyroomIDs, averageDataIDs

#trata dados
def handle_data():
    while(True):
        try:
            insertRep()
            insertAPI()
            insertServer()
            time.sleep(600)
        except:
            print("failed: handle_data")
            continue

def handle_api():
    while(True):
        try:
            insertRoomAPIs()
            insertParqAPI()
            time.sleep(600)
        except:
            print("failed: apis")
            continue

def handle_average():
    while(True):
        try:
            insertAverage()
            time.sleep(3000) #nao ha necessidade de correr em menos do que quase hora a hora
        except:
            print("failed: handle average")
            continue

def insertRep():
    try:
        valor = convertToValue()

        #trata da inserção dos valores na base de dados nas tabelas respetivas
        mydb = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="smartUMarep"
        )

        insertSQL(mydb, valor)
    except:
        print("failed: insert rep")

#insert on database
def insertSQL(mydb, valor):
    try:
        with closing( mydb.cursor() ) as mycursor:
            mycursor = mydb.cursor()

            print(datetime.now()) #debug para o timestamp
            tim = datetime.now()
            valor.append('{:%Y-%m-%d %H:%M:%S}'.format(tim))
            
            convert_direction(valor)   

            sql = "INSERT INTO weather_weather (temperature, humidity, wind_speed, wind_direction, solar_intensity, timestamp) VALUES ("+str(valor[0])+", "+str(valor[1])+", "+str(valor[3])+", %s, "+str(valor[2])+", %s)"
            val = (valor[4],valor[5])

            mycursor.execute(sql,val)
            mydb.commit()

        mydb.close()
    except:
        print("failed: insertSQL")

#trata da base de dados da API (escrita)
def insertAPI():
    try:
        valor = convertToValue()

        mydb = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="smartUMarep"
        )
        
        with closing( mydb.cursor() ) as mycursor:
            mycursor = mydb.cursor()

            print(datetime.now()) #debug para o timestamp
            tim = datetime.now()
            valor.append('{:%Y-%m-%d %H:%M:%S}'.format(tim))
            
            convert_direction(valor)   

            #query a base de dados para ver se existe valores na tabela da API
            mycursor.execute("SELECT * FROM api_weather")
            myresult = mycursor.fetchall()
            
            if len(myresult) > 0:
                sql = "UPDATE api_weather SET temperature = "+str(valor[0])+" , humidity = "+str(valor[1])+", wind_speed = "+str(valor[3])+", wind_direction = '"+str(valor[4])+"', solar_intensity = "+str(valor[2])+", timestamp = %s WHERE id = 1"
                val = valor[5]

                mycursor.execute(sql,val)
                mydb.commit()

                send_data(sql)

            else:
                sql = "INSERT INTO api_weather (temperature, humidity, wind_speed, wind_direction, solar_intensity, timestamp) VALUES ("+str(valor[0])+", "+str(valor[1])+", "+str(valor[3])+", '"+str(valor[4])+"', "+str(valor[2])+", %s)"
                val = valor[5]
                mycursor.execute(sql,val)
                mydb.commit() 

                #envia pelo socket
                send_data(sql)      

        mydb.close()
    except:
        print("failed: inserting api rep")

#trata da base de dados principal (escrita)
def insertServer():
    try:
        valor = convertToValue()

        #add time
        tim = datetime.now()
        valor.append('{:%Y-%m-%d %H:%M:%S}'.format(tim))
        
        #set wind direction
        convert_direction(valor)

        sql = "INSERT INTO weather_weather (temperature, humidity, wind_speed, wind_direction, solar_intensity, timestamp) VALUES ("+str(valor[0])+", "+str(valor[1])+", "+str(valor[3])+", '"+str(valor[4])+"', "+str(valor[2])+", %s)"
        
        send_data(sql)
    except:
        print("failed: sending through socket")

#socket para inserção de dados proprios
def send_data(sql):
    try:
        print(sql)
        #insert through socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(('localhost', 50000))

        s.send(str.encode(sql))

        s.close()
    except:
        print("failed: sending through socket normal insert")

#socket para inserção de dados extenos
def send_data_api(sql):
    try:
        print(sql)
        #insert through socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(('localhost', 50001))

        s.send(str.encode(sql))

        s.close()
    except:
        print("failed: sending through socket api insert")

#socket para inserção das médias
def send_data_average(sql):
    try:
        print(sql)
        #insert through socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(('localhost', 50002))

        s.send(str.encode(sql))

        s.close()
    except:
        print("failed: sending through socket average insert")

#set wind direction
def convert_direction(valor):
    try:
        if valor[4] >= 0.0 and valor[4] < 45.0:
                valor[4] = 'N'
                return
        if valor[4] >= 45.0 and valor[4] < 90.0:
                valor[4] = 'NE'
                return
        if valor[4] >= 90.0 and valor[4] < 135.0:
                valor[4] = 'E'
                return
        if valor[4] >= 135.0 and valor[4] < 180.0:
                valor[4] = 'SE'
                return
        if valor[4] >= 180.0 and valor[4] < 225.0:
                valor[4] = 'S'
                return
        if valor[4] >= 225.0 and valor[4] < 270.0:
                valor[4] = 'SW'
                return
        if valor[4] >= 270.0 and valor[4] < 315.0:
                valor[4] = 'W'   
                return
        if valor[4] >= 315.0 and valor[4] < 361.0:
                valor[4] = 'NW'  
                return
    except:
        print("failed : convert into Orientations")

#Api net status
def insertRoomAPIs():
    try:
        valor = netNtempAPI()
        salasocup = studyRoomSeatsAPI()
        salasnoise = noiseAPI()

        sql = "INSERT INTO network_network (latency, download_speed, upload_speed, timestamp) VALUES ("+str(valor[0])+", "+str(valor[1])+", "+str(valor[2])+", %s)"
        insertExternalAPi(sql)

        ## SALA 0 ##
        sql = "INSERT INTO studyroom_studyroom (temperature, occupation, noise, room, timestamp) VALUES ("+str(valor[3])+","+str(salasocup[0])+", "+str(salasnoise[0])+", 0 , %s)"
        insertExternalAPi(sql)
        
        ## SALA 1 ##
        sql = "INSERT INTO studyroom_studyroom (temperature, occupation, noise, room, timestamp) VALUES ("+str(valor[4])+","+str(salasocup[1])+", "+str(salasnoise[1])+", 1 , %s)"
        insertExternalAPi(sql)
        
        ## SALA 2 ##
        sql = "INSERT INTO studyroom_studyroom (temperature, occupation, noise, room, timestamp) VALUES ("+str(valor[5])+","+str(salasocup[2])+", "+str(salasnoise[2])+", 2 , %s)"
        insertExternalAPi(sql)
        
        ## SALA 2-PC ##
        sql = "INSERT INTO studyroom_studyroom (temperature, occupation, noise, room, timestamp) VALUES ("+str(valor[5])+","+str(salasocup[2])+", "+str(salasnoise[2])+", '2-PC' , %s)"
        insertExternalAPi(sql)
        
        ## SALA 3 ##
        sql = "INSERT INTO studyroom_studyroom (temperature, occupation, noise, room, timestamp) VALUES ("+str(valor[6])+","+str(salasocup[3])+", "+str(salasnoise[3])+", 3 , %s)"
        insertExternalAPi(sql)
        
    except:
        print("failed: room apis")        
        
#Api parque        
def insertParqAPI():
    try:
        parque = parkingAPI()
        sql = "INSERT INTO parking_parking (occupation, timestamp) VALUES ("+str(parque)+", %s)"
        insertExternalAPi(sql)
    except:
        print("failed: park ocupation")

def insertExternalAPi(sql):
    try:
        mydb = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="smartUMarep"
        )
        #add time
        tim = datetime.now()
        currentTime = ('{:%Y-%m-%d %H:%M:%S}'.format(tim))

        with closing( mydb.cursor() ) as mycursor:
            mycursor = mydb.cursor()
            
            mycursor.execute(sql,currentTime)
            mydb.commit()

            #envia pelo socket
            send_data_api(sql) 
            time.sleep(5)
    except:
        print("failed: connect db for ext api")

def insertAverage():
    try:
        averageWeather = getValuesWeather()
        averageParking = getValuesParking()
        averageNetwork = getValuesNetwork()
        averageRoom0 = getValuesStudyRoom("0") 
        averageRoom1 = getValuesStudyRoom("1") 
        averageRoom2 = getValuesStudyRoom("2") 
        averageRoom3 = getValuesStudyRoom("3") 

        mydb = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="smartUMarep"
        )

        with closing( mydb.cursor() ) as mycursor:
            mycursor = mydb.cursor()

            now = datetime.datetime.now()
            newday = now.replace(hour=0, minute=0, second=0, microsecond=0)
            oneAM = now.replace(hour=1, minute=0, second=0, microsecond=0)

            #compara hora atual com 00:00 e 01:00
            if((now > newday and now < oneAM) or now == newday):
                ## weather ##
                sql = "INSERT INTO averagedata_weather (temperature, humidity, wind_speed, wind_direction, solar_intensity) VALUES ("+str(averageWeather[0])+", "+str(averageWeather[1])+", "+str(averageWeather[2])+","+str(averageWeather[3])+","+str(averageWeather[4])+")"
                mycursor.execute(sql)
                mydb.commit()
                send_data_average(sql)
                time.sleep(5)

                ## SALAS ##
                sql = "INSERT INTO averagedata_floor0 (temperature, occupation, noise) VALUES ("+str(averageRoom0[0])+", "+str(averageRoom0[1])+", "+str(averageRoom0[2])+")"
                mycursor.execute(sql)
                mydb.commit()
                send_data_average(sql)
                time.sleep(5)

                sql = "INSERT INTO averagedata_floor1 (temperature, occupation, noise) VALUES ("+str(averageRoom1[0])+", "+str(averageRoom1[1])+", "+str(averageRoom1[2])+")" 
                mycursor.execute(sql)
                mydb.commit()
                send_data_average(sql)
                time.sleep(5)

                
                sql = "INSERT INTO averagedata_floor2 (temperature, occupation, noise) VALUES ("+str(averageRoom2[0])+", "+str(averageRoom2[1])+", "+str(averageRoom2[2])+")"
                mycursor.execute(sql)
                mydb.commit()
                send_data_average(sql)
                time.sleep(5)
                
                
                sql = "INSERT INTO averagedata_floor2pc (temperature, occupation, noise) VALUES ("+str(averageRoom2[0])+", "+str(averageRoom2[1])+", "+str(averageRoom2[2])+")"
                mycursor.execute(sql)
                mydb.commit()
                send_data_average(sql)
                time.sleep(5)
                
                
                sql = "INSERT INTO averagedata_floor3 (temperature, occupation, noise) VALUES ("+str(averageRoom3[0])+", "+str(averageRoom3[1])+", "+str(averageRoom3[2])+")"
                mycursor.execute(sql)
                mydb.commit()
                send_data_average(sql)
                time.sleep(5)
                
                ## Network ##
                sql = "INSERT INTO averagedata_network (latency, download_speed, upload_speed) VALUES ("+str(averageNetwork[0])+","+str(averageNetwork[1])+", "+str(averageNetwork[2])+")"
                mycursor.execute(sql)
                mydb.commit()
                send_data_average(sql)
                time.sleep(5)
                
                ## Parking ##
                sql = "INSERT INTO averagedata_parking(occupation) VALUES ("+str(averageParking)+")"
                mycursor.execute(sql)
                mydb.commit()
                send_data_average(sql)
                time.sleep(5)
                
                # inserção de averagedata_studyroom é necessário ser apôs as outras
                room_ids = averageStudyroomIDs()
                sql = "INSERT INTO averagedata_studyroom (studyroom0_id, studyroom1_id, studyroom2_id, studyroom2PC_id, studyroom3_id) VALUES ('"+str(room_ids[0])+"', '"+str(room_ids[1])+"', '"+str(room_ids[2])+"', '"+str(room_ids[3])+"', '"+str(room_ids[4])+"')"
                mycursor.execute(sql)
                mydb.commit()
                send_data_average(sql)
                time.sleep(5)

                # inserção de averagedata_averagedata necessita de ser realisada apôs a actualização da restantes averages
                data_ids = averageDataIDs()
                sql = "INSERT INTO averagedata_averagedata (timestamp, network_id, parking_id, studyroom_id, weather_id) VALUES ('%s', '1', '1', '1', '1')"
                mycursor.execute(sql, now)
                mydb.commit()
                send_data_average(sql)
                time.sleep(5)

        mydb.close()



    except:
        print("failed: insert average")


#create thread
thread = Timer(1, handle_data)
api_thread = Timer(5, handle_api)
average_thread = Timer(10,handle_average)

thread.start()
api_thread.start()
average_thread.start()
