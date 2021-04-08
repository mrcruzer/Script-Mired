from datetime import datetime, timedelta
import mysql.connector
from mysql.connector import errorcode
from Movimiento import Movimientos
from MovExcel import MovimientoExcel

config ={
         'host':'localhost',
         'user':'root',
         'password':'',
         'database':'test',
         'raise_on_warnings':True,

       }

cursor = 0
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    query = "SELECT \
                DATE_FORMAT(reportsab.FECHA,'%d-%m-%y')as fecha,\
                    reportsab.CUC,\
                    reportsab.SAB, \
                    reportsab.TERMINAL,\
                    reportsab.MONTO  \
                    FROM \
                    reportsab \
                WHERE WEEK(reportsab.FECHA) = (WEEKOFYEAR(curdate()``)) \
                ORDER BY reportsab.CUC,reportsab.FECHA" 


    cursor.execute(query)
    m2e = MovimientoExcel(' Report')
    
    for fila in cursor:
        reportsab = Movimientos(fila)
        reportsab.lista()

        m2e.agregarItem(reportsab)

        m2e.guardarPlantilla("ejemplo.xls")

except mysql.connector.Error as err:
            if err.errno ==errorcode.ER_ACCESS_DENIED_ERROR:
                print("error ")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                 print("DATABASE NO EXISTE")

            else:
                    print(err) 
else:
                      cnx.close()   
                   

         