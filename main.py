import pymysql
cnn = pymysql.connect(
     host="localhost",
               user="root",
                password="",
                database="test"
)


cur = cnn.cursor()
cur.execute("SELECT * FROM  reportsab ")
datos = cur.fetchall()

for fila in datos:
    print(fila)
