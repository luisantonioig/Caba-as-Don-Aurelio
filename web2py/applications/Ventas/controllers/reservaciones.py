def index():
    return 'hola si funciona o no'

def reservaciones():
    reserva=SQLFORM(db.reservacion)
    reserva[0][4][1][0]=INPUT(_type='text', _class='double form-control',_id='reservacion_precio',_name='precio',_onkeyup='sumar();')
    reserva[0][5][1][0]=INPUT(_type='text', _class='double form-control',_id='reservacion_anticipo',_name='anticipo',_onkeyup='sumar();', _value='0')
    print ''
    if reserva.process().accepted:
        response.flash = 'Ok!!'
    elif reserva.errors:
        response.flash = 'Tienes errores en los datos'
    else:
        response.flash = 'Por favor llena los datos del cliente'
    return dict(reserva=reserva)

def reservaciones_existentes():
    return dict()
