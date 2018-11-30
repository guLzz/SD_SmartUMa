import time
from threading import *
from ModuloDB import *

#trata dados e envia para a replicacao
def handle_data():   
    sql = convert_insert()
    db_data(sql)

#trata da base de dados principal (escrita)
def db_data(sql):
    mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="smartuma"
    )
    valor = []
    tim = datetime.now()
    valor.append('{:%Y-%m-%d %H:%M:%S}'.format(tim))
    val = (valor[0])

    mycursor = mydb.cursor()
    mycursor.execute(sql,val)
    mydb.commit()

#trata pedidos do servidor 
def listen_request():
    return False

#create thread
thread = Timer(10, handle_data)
thread_listen = Timer(5,listen_request)

thread.start()
thread_listen.start()