import time
import pymysql.cursors
import socket

from threading import *
from contextlib import closing
from datetime import datetime

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 50000        # Port to listen on (non-privileged ports are > 1023)

 
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
    
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
                database="smartuma"
                )
                sql = data.decode()
                tim = datetime.now()
                valor = ('{:%Y-%m-%d %H:%M:%S}'.format(tim))
                

                with closing( mydb.cursor() ) as mycursor:
                    mycursor = mydb.cursor()
                
                    mycursor.execute(sql,valor)
                    mydb.commit()

                mydb.close()
