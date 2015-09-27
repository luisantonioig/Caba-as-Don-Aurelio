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
    import time
    meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    month_and_year= meses[int(time.strftime("%m"))-1] + " del 20"+ time.strftime("%y")
    cabecera = SPAN(month_and_year)
    dias = ['lu','ma','mi','ju','vi','sa','do']
    etiqueta_dias = TR()
    tabla = TABLE()
    for dia in dias:
        etiqueta_dias.append(TD(dia,_style="padding:5px;"))
    tabla.append(etiqueta_dias)
    import calendar
    primer_dia = calendar.monthrange(int("20"+time.strftime("%y")),int(time.strftime("%m")))
    etiqueta_dias=TR()
    contador = 0
    for numero in range(primer_dia[0]):
        contador = contador +1
        etiqueta_dias.append(TD(str("")))
    for numero in range(primer_dia[1]):
        if numero==int(time.strftime("%d"))-1:
            etiqueta_dias.append(TD(str(numero+1),_align="center",_bgcolor="red"))
        else:
            etiqueta_dias.append(TD(str(numero+1),_align="center"))
        contador = contador + 1
        if contador==7:
            tabla.append(etiqueta_dias)
            etiqueta_dias = []
            contador=0
    tabla.append(etiqueta_dias)
    print primer_dia
    return dict(cabecera=cabecera, tabla=tabla)
