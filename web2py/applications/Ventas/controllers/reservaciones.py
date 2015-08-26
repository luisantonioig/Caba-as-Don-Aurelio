def index():
    return 'hola si funciona o no'

def reservaciones():
    reserva=SQLFORM(db.reservacion)
    if reserva.process().accepted:
        response.flash = 'Ok!!'
    elif reserva.errors:
        response.flash = 'Tienes errores en los datos'
    else:
        response.flash = 'Por favor llena los datos del cliente'
    return dict(reserva=reserva)

def reservaciones_existentes():
    return dict()
