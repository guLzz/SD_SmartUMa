import time
import pymysql.cursors

from threading import *
from contextlib import closing
from datetime import datetime
from ModuloDB import convertToValue

#trata dados e envia para a replicacao
def handle_data():   
    while(True):
        insertRep()
        insertServer()
        time.sleep(60)

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



def insertSQL(mydb, valor):
    with closing( mydb.cursor() ) as mycursor:
        mycursor = mydb.cursor()

        print(datetime.now()) #debug para o timestamp
        tim = datetime.now()
        valor.append('{:%Y-%m-%d %H:%M:%S}'.format(tim))
        
        sql = "INSERT INTO weather_weather (temperature, humidity, wind_speed, wind_direction, solar_intensity, timestamp) VALUES ("+str(valor[0])+", "+str(valor[1])+", "+str(valor[3])+", "+str(valor[4])+", "+str(valor[2])+", %s)"
        val = (valor[5])

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