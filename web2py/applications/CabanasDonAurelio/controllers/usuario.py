# -*- coding: utf-8 -*-
# intente algo como
from gluon.tools import Mail
mail = Mail()
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'antonio.ibarra.g46@gmail.com'
mail.settings.login = 'antonio.ibarra.g46:qnzsymccqgnogxyg'

def index(): return dict(message="hello from usuario.py")

def info():
    return dict(hola="hola")

def send_email():
    mensaje = 'Nombre: '+request.vars.nombre+' '+request.vars.apellidos+'\ne-Mail: '+request.vars.email+ '\nComentario: '+request.vars.comentarios
    if mail.send(to=['c-remix@hotmail.es'],
          subject='Comentarios de "Cabañas Don Aurelio"',
          # If reply_to is omitted, then mail.settings.sender is used
          message=mensaje):
        session.flash = "Mensaje enviado"
    else:
        session.flash= "No se pudo enviar el mensaje"
    redirect(URL('info'))
