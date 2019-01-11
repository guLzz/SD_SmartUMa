import time
import pymysql.cursors

from contextlib import closing

def refillDB():
    try:
        
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="smartuma" #smartUMa
            )
        
        print("debug1")

        with closing( mydb.cursor() ) as mycursor:
            mycursor = mydb.cursor()
            sql = "SELECT * FROM weather_weather"
            mycursor.execute(sql)

            print("debug2")

            myresult = mycursor.fetchall()

            print(myresult)
            print(myresult[0])
            
            array = [float(myresult[0][1]), float(myresult[0][2]), float(myresult[0][3]), myresult[0][4], float(myresult[0][5])]

            print(array)
    except:
        print("failed: refill Database")

if __name__ == "__main__":
    refillDB()