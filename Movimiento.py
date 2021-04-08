class Movimientos(object):

         def __init__(self,lista):

                    self.FECHA =lista[0]
                    self.CUC =lista[1]
                    self.SAB = lista[2]
                    self.TERMINAL =lista[3]
                    self.MONTO =str( lista[4])
         def lista(self):
                print(self.FECHA,self.CUC,self.SAB,self.TERMINAL,self.MONTO)
