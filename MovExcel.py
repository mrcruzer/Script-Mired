import xlwt
from datetime import datetime
import win32com.client as win32
from xlutils.copy import copy
from xlrd import *

class MovimientoExcel:

    def __init__(self,name):
            self.wb = xlwt.Workbook()
            self.ws = self.wb.add_sheet(name,cell_overwrite_ok=True)
            
            self.excel = win32.dispatchEX('Excel.Application')
            self.excel.DisplayAlerts = False
            self.excel.Visible = True
            
            self.xlfinal = self.ws 
            self.xlfinal.RefreshAll()
            
            

            self.ws.write(0, 0, name)

            columnas =[     
                            "FECHA",
                            "CUC",
                            "SAB",
                            "TERMINAL",
                            "MONTO"]


            C = 0
            for columna in columnas:
                  self.ws.write(1, C, columna)   
                  C = C + 1

            self.fila = 1

    def agregarItem(self,item):   
         self.ws.write(self.fila, 0, item.FECHA)
         self.ws.write(self.fila, 1, item.CUC)  
         self.ws.write(self.fila, 2, item.SAB)   
         self.ws.write(self.fila, 3, item.TERMINAL)
         self.ws.write(self.fila, 4, item.MONTO)  

         self.fila = self.fila + 1

    def guardarPlantilla(self,archivo):
        self.xlfinal.Save(archivo)
        self.xlfinal.Close()
        #self.wb.write(archivo)
        
        print("Generado")     









            
        


