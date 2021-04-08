import time
class Mensaje(object):

    def __init__(self,inicio,fin):

        self.subject = "Reporte semanal de TXN" +inicio+"  "+fin 
        self.subject = time.strftime("Reporte diarios" +' '+"%I:%M:%S")

        self.head = "<html><h2><b>Reporte "+inicio+" - "+fin+"</b></h2>"
        self.body = "<p>Adjunto de archivo xls.</p>"
            

        self.tail = '<p>Datos</p></html>'

    def getMensaje(self):
        return self.head+self.body+self.tail
    

    def agregarContenido(self,data):
        self.body = self.body + data