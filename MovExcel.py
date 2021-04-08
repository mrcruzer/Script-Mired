import xlwt
from datetime import datetime

class MovimientoExcel:

    def __init__(self,name):
            self.wb = xlwt.Workbook()
            self.ws = self.wb.add_sheet(name,cell_overwrite_ok=True)

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

            self.fila = 2

    def agregarItem(self,item):   
         self.ws.write(self.fila, 0, item.FECHA)
         self.ws.write(self.fila, 1, item.CUC)  
         self.ws.write(self.fila, 2, item.SAB)   
         self.ws.write(self.fila, 3, item.TERMINAL)
         self.ws.write(self.fila, 4, item.MONTO)  

         self.fila = self.fila + 1

    def guardarPlantilla(self,archivo):
        self.wb.save(archivo)
        print("Generado")     









            
        


