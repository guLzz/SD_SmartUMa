import time
import pymysql.cursors

from threading import *
from contextlib import closing
from datetime import datetime
from ModuloDB import convertToValue

#trata dados e envia para a replicacao
def handle_data():   
    #while(True):
        insertRep()
        insertAPI()
		#insertServer()
        #time.sleep(60)

def insertRep():

    valor = convertToValue ()

    #trata da inserção dos valores na base de dados nas tabelas respetivas
    mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="smartumarep"
    )

    insertSQL(mydb, valor)
    
#trata da base de dados da API (escrita)
def insertAPI():
    valor = convertToValue()

    mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="smartumarep"
    )
    
    with closing( mydb.cursor() ) as mycursor:
        mycursor = mydb.cursor()

        print(datetime.now()) #debug para o timestamp
        tim = datetime.now()
        valor.append('{:%Y-%m-%d %H:%M:%S}'.format(tim))
        
        convert_direction(valor)   

        sql = "INSERT INTO api_weather (temperature, humidity, wind_speed, wind_direction, solar_intensity, timestamp) VALUES ("+str(valor[0])+", "+str(valor[1])+", "+str(valor[3])+", %s, "+str(valor[2])+", %s)"
        val = (valor[4],valor[5])

        mycursor.execute(sql,val)
        mydb.commit()

    mydb.close()


#trata da base de dados principal (escrita)
def insertServer():
    valor = convertToValue()

    mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="smartuma"
    )
    
    insertSQL(mydb, valor)

def convert_direction(valor):
        if valor[4] > 0.0 and valor[4] < 45.0:
                valor[4] = 'N'
                return
        if valor[4] > 45.0 and valor[4] < 90.0:
                valor[4] = 'NE'
                return
        if valor[4] > 90.0 and valor[4] < 135.0:
                valor[4] = 'E'
                return
        if valor[4] > 135.0 and valor[4] < 180.0:
                valor[4] = 'SE'
                return
        if valor[4] > 180.0 and valor[4] < 225.0:
                valor[4] = 'S'
                return
        if valor[4] > 225.0 and valor[4] < 270.0:
                valor[4] = 'SW'
                return
        if valor[4] > 270.0 and valor[4] < 315.0:
                valor[4] = 'W'   
                return
        if valor[4] > 315.0 and valor[4] < 361.0:
                valor[4] = 'NW'  
                return

def insertSQL(mydb, valor):
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
    
#trata pedidos do servidor 
def listen_request():
    return False

#create thread
thread = Timer(10, handle_data)
thread_listen = Timer(5,listen_request)

thread.start()
thread_listen.start()