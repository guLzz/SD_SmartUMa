import time
import pymysql.cursors
import socket

from threading import *
from contextlib import closing
from datetime import datetime
from ModuloDB import convertToValue

#trata dados
def handle_data():   
    #while(True):
        insertRep()
        insertAPI()
        insertServer()
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

#insert on database
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

        #query a base de dados para ver se existe valores na tabela da API
        mycursor.execute("SELECT * FROM api_weather")
        myresult = mycursor.fetchall()
        
        if len(myresult) > 0:
            sql = "UPDATE api_weather SET temperature = "+str(valor[0])+" , humidity = "+str(valor[1])+", wind_speed = "+str(valor[3])+", wind_direction = '"+valor[4]+"', solar_intensity = "+str(valor[2])+", timestamp = %s WHERE id = 1"
            val = valor[5]

            mycursor.execute(sql,val)
            mydb.commit()

            send_data(sql)

        else:
            sql = "INSERT INTO api_weather (temperature, humidity, wind_speed, wind_direction, solar_intensity, timestamp) VALUES ("+str(valor[0])+", "+str(valor[1])+", "+str(valor[3])+", '"+valor[4]+"', "+str(valor[2])+", %s)"
            val = valor[5]
            mycursor.execute(sql,val)
            mydb.commit() 

            #envia pelo socket
            send_data(sql)      

    mydb.close()


#trata da base de dados principal (escrita)
def insertServer():
    valor = convertToValue()

    #add time
    tim = datetime.now()
    valor.append('{:%Y-%m-%d %H:%M:%S}'.format(tim))
    
    #set wind direction
    convert_direction(valor)

    sql = "INSERT INTO weather_weather (temperature, humidity, wind_speed, wind_direction, solar_intensity, timestamp) VALUES ("+str(valor[0])+", "+str(valor[1])+", "+str(valor[3])+", '"+valor[4]+"', "+str(valor[2])+", %s)"
    
    send_data(sql)

def send_data(sql):
    print(sql)
    #insert through socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(('localhost', 50000))

    s.send(str.encode(sql))

    s.close()
    
#set wind direction
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


    
#trata pedidos do servidor 
def listen_request():
    return False

#create thread
thread = Timer(10, handle_data)
#thread_listen = Timer(5,listen_request)

thread.start()
#thread_listen.start()