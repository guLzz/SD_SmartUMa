import time
import pymysql.cursors
import socket

from threading import *
from contextlib import closing
from datetime import datetime

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)#
WEATHER_PORT = 50000        # Port to listen on (non-privileged ports are > 1023)
API_PORT = 50001
AVERAGE_PORT = 50002

def listen_weather():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_weather:
                s_weather.bind((HOST, WEATHER_PORT))
                s_weather.listen()
                conn, addr = s_weather.accept()
            
                with conn:
                    print('Connected by', addr)
                    
                    data = conn.recv(1024)
                    print(data.decode())
                    if not data:
                        time.sleep(10)
                    else:
                        #insert sql
                        mydb = pymysql.connect(
                        host="localhost",
                        user="root",
                        passwd="",
                        database="smartUMa"
                        )
                        sql = data.decode()
                        tim = datetime.now()
                        valor = ('{:%Y-%m-%d %H:%M:%S}'.format(tim))
                        

                        with closing( mydb.cursor() ) as mycursor:
                            mycursor = mydb.cursor()
                        
                            mycursor.execute(sql,valor)
                            mydb.commit()

                            mydb.close()
        except:
            print("failed: listen average")
            continue

def listen_api():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_api:
                s_api.bind((HOST, API_PORT))
                s_api.listen()
                conn, addr = s_api.accept()
            
                with conn:
                    print('Connected by', addr)
                    
                    data = conn.recv(1024)
                    print(data.decode())
                    if not data:
                        time.sleep(10)
                    else:
                        #insert sql
                        mydb = pymysql.connect(
                        host="localhost",
                        user="root",
                        passwd="",
                        database="smartUMa"
                        )
                        sql = data.decode()
                        tim = datetime.now()
                        valor = ('{:%Y-%m-%d %H:%M:%S}'.format(tim))
                        

                        with closing( mydb.cursor() ) as mycursor:
                            mycursor = mydb.cursor()
                        
                            mycursor.execute(sql,valor)
                            mydb.commit()

                            mydb.close()
        except:
            print("failed: listen average")
            continue

def listen_average():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_average:
                s_average.bind((HOST, AVERAGE_PORT))
                s_average.listen()
                conn, addr = s_average.accept()
            
                with conn:
                    print('Connected by', addr)
                    
                    data = conn.recv(1024)
                    print(data.decode())
                    if not data:
                        time.sleep(10)
                    else:
                        msg = data.decode()

                        #find() se nao encontrar devolve -1
                        if(msg.find("%s") != -1):
                            #insert sql with timestamp
                            mydb = pymysql.connect(
                            host="localhost",
                            user="root",
                            passwd="",
                            database="smartUMa"
                            )
                            sql = data.decode()
                            tim = datetime.now()
                            valor = ('{:%Y-%m-%d %H:%M:%S}'.format(tim))
                        

                            with closing( mydb.cursor() ) as mycursor:
                                mycursor = mydb.cursor()
                            
                                mycursor.execute(sql,valor)
                                mydb.commit()

                                mydb.close()

                        else:
                            #insert sql sem timestamp
                            mydb = pymysql.connect(
                            host="localhost",
                            user="root",
                            passwd="",
                            database="smartUMa"
                            )
                            sql = data.decode()
                        
                            with closing( mydb.cursor() ) as mycursor:
                                mycursor = mydb.cursor()
                            
                                mycursor.execute(sql)
                                mydb.commit()

                                mydb.close()
        except:
            print("failed: listen average")
            continue

#create thread
weather_thread = Timer(5, listen_weather)
api_thread = Timer(5, listen_api)
average_thread = Timer(5, listen_average)

weather_thread.start()
api_thread.start()
average_thread.start()