# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from cliente.py")

def nuevo():
    formulario = SQLFORM(db.cliente)
    if formulario.process().accepted:
        response.flash = 'Ok!!'
    elif formulario.errors:
        response.flash = 'Tienes errores en los datos'
    else:
        response.flash = 'Por favor llena los datos del cliente'
    return dict(Nuevo_cliente = formulario)

def ver_clientes():
    grid = SQLFORM.grid(db.cliente)
    return dict(grid=grid)

def ver_cliente():
    clave = request.vars.id
    datos = db(db.cliente.id==clave).select(db.cliente.ALL)
    reservaciones = db(db.reservacion.cliente==clave).select(db.reservacion.ALL)
    print reservaciones
    return dict(datos = datos, reservaciones=reservaciones)
