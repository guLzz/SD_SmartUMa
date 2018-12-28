import time
import pymysql.cursors
import socket

from threading import *
from contextlib import closing
from datetime import datetime
from ModuloDB import convertToValue
from apis import parkingAPI,netNtempAPI,studyRoomSeatsAPI,noiseAPI

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


def send_data(sql):
    try:
        print(sql)
        #insert through socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(('localhost', 50000))

        s.send(str.encode(sql))

        s.close()
    except:
        print("failed: sending through socket")

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
            send_data(sql) 
            time.sleep(5)
    except:
        print("failed: connect db for ext api")

#create thread
thread = Timer(1, handle_data)
api_thread = Timer(5, handle_api)

thread.start()
api_thread.start()
