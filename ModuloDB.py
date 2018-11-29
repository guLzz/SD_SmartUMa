import pandas as pd
import json
from collections import namedtuple
import re
import pymysql as mysql
import datetime

#funcao para retornar apenas floats 
def get_num(x):
    return float(''.join(ele for ele in x if ele.isdigit() or ele == '.'))


def convert_insert():
    
    calls_df, = pd.read_html("http://www.cee.uma.pt/hardlab/wsngroup/wsn/realtimeinfo.php", header=0,attrs = {'width': '230', 'style': 'font-size:small;color:#333333;'}) #acede tabela com atributos especificados no site especificado

    data = calls_df.to_json(orient="records", date_format="iso") #transforma dados em formato json
    print(data) #debug
    #GUARDAR COMO FICHEIRO .json para fazer a API com isso
    values = json.loads(data) #carrega json como objeto

    print(type(values)) #debug para saber tipo do json

    valor = []

    for value in values:
        print(get_num(value['Unnamed: 1'])) #imprime valor dentro do unnamed1 usando a função get_enum para retirar unidades
        valor.append(get_num(value['Unnamed: 1']))

    print(datetime.datetime.now()) #debug para o timestamp  

    #trata da inserção dos valores na base de dados nas tabelas respetivas
    mydb = mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO Metereologia (temperatura, humidade, radiacao, velocidade_vento, direcao_vento, timestamp) VALUES ("+str(valor[0])+", "+str(valor[1])+", "+str(valor[2])+", "+str(valor[3])+", "+str(valor[4])+", "+str(datetime.datetime.now())+")"
    #val = (valor[0],valor[1],valor[2],valor[3], valor[4])

    #debug da query
    #print(sql)

    mycursor.execute(sql)
    mydb.commit()   

    return sql


#Serve apenas para debug, sendo que todo o codigo sera chamado noutro sitio
if __name__ == "__main__":
    convert_insert()

