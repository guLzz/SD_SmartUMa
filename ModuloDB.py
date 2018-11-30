import pandas as pd
import json
from collections import namedtuple
import re
import time

#funcao para retornar apenas floats 
def get_num(x):
    return float(''.join(ele for ele in x if ele.isdigit() or ele == '.'))


def convertToValue():
    
    calls_df, = pd.read_html("http://www.cee.uma.pt/hardlab/wsngroup/wsn/realtimeinfo.php", header=0,attrs = {'width': '230', 'style': 'font-size:small;color:#333333;'}) #acede tabela com atributos especificados no site especificado

    data = calls_df.to_json(orient="records", date_format="iso") #transforma dados em formato json
    print(data) #debug
    #GUARDAR COMO FICHEIRO .json para fazer a API com isso
    values = json.loads(data) #carrega json como objeto

    valor = []

    for value in values:
        print(get_num(value['Unnamed: 1'])) #imprime valor dentro do unnamed1 usando a função get_enum para retirar unidades
        valor.append(get_num(value['Unnamed: 1']))        

    return valor

#Serve apenas para debug, sendo que todo o codigo sera chamado noutro sitio
#if __name__ == "__main__":
#    convert_insert()

