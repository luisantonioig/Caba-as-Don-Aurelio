def index():
    return 'hola si funciona o no'

def reservaciones():
    reserva=SQLFORM(db.reservacion)
    return dict(reserva=reserva)

def reservaciones_existentes():
    return dict()
