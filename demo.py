from EnvMail import EnvMail

from Mensaje import Mensaje

import time


msg = Mensaje('','')
#print (time.strftime("%d/%m/%y"))
#contenido al mensaje en formato html
msg.agregarContenido("<p>Report Txn </p>")

#agregamos un imagen al mensaje 
msg.agregarContenido("<p><img src=\"http://www.gsampallo.com/blog/wp-content/uploads/2019/07/logo-gs_logo-fondo-negro.jpg\" height=\"15%\"	width=\"15%\"></p>")

mMail = EnvMail()

mMail.destinatarios.append("mired1225@gmail.com")
#mMail.destinatarios.append("")


mMail.enviarCorreo(msg,"ejemplo.xls")