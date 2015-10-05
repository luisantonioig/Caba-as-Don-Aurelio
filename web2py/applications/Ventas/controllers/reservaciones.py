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
    year = "20"+ time.strftime("%y")
    if request.vars['year']:
        year = request.vars['year']
    consulta = db.executesql('SELECT fecha_inicio,fecha_fin FROM reservacion where fecha_inicio like "%'+year+'%";')
    meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    calendario = DIV(_id="calendario-"+year)
    for mes in meses:
        month_and_year= mes + " del "+year
        cabecera = DIV(_id=mes)
        if mes != "Enero":
            boton_anterior = SPAN(A(IMG(_id="mes_anterior",_src='../static/images/anterior.png',_WIDTH=30, _height=30)),_onClick="atras(this.id);",_id=mes)
        else:
            boton_anterior = SPAN(A(IMG(_id="mes_anterior",_src='../static/images/anterior.png',_WIDTH=30, _height=30)),_id=mes)
        leyenda = SPAN(month_and_year)
        if mes != "Diciembre":
            boton_siguiente = SPAN(A(IMG(_id="siguiente",_src='../static/images/siguiente.png',_WIDTH=30, _height=30)),_onClick="adelante(this.id);",_id=mes)
        else:
            boton_siguiente = SPAN(A(IMG(_id="mes_siguiente",_src='../static/images/siguiente.png',_WIDTH=30, _height=30)),_id=mes)
        cabecera.append(boton_anterior)
        cabecera.append(leyenda)
        cabecera.append(boton_siguiente)
        dias = ['lu','ma','mi','ju','vi','sa','do']
        etiqueta_dias = TR()
        tabla = TABLE()
        for dia in dias:
            etiqueta_dias.append(TD(dia,_style="padding:5px;"))
        tabla.append(etiqueta_dias)
        import calendar
        primer_dia = calendar.monthrange(int(year),meses.index(mes)+1)
        etiqueta_dias=TR()
        contador = 0
        for numero in range(primer_dia[0]):
            contador = contador +1
            etiqueta_dias.append(TD(str("")))
        for numero in range(primer_dia[1]):
            bandera = False
            for reservacion in consulta:
                if int(reservacion[0].strftime("%m"))==meses.index(mes)+1 and int(reservacion[0].strftime("%d"))==numero+1:
                    bandera=True
            if bandera:
                etiqueta_dias.append(TD(str(numero+1),_align="center",_bgcolor="blue"))
            elif numero==int(time.strftime("%d"))-1 and meses.index(mes)==int(time.strftime("%m"))-1 and year==int("20"+time.strftime("%y")):
                etiqueta_dias.append(TD(str(numero+1),_align="center",_bgcolor="red"))
            else:
                etiqueta_dias.append(TD(str(numero+1),_align="center"))
            contador = contador + 1
            if contador==7:
                tabla.append(etiqueta_dias)
                etiqueta_dias = []
                contador=0
        tabla.append(etiqueta_dias)
        cal_cabezera = DIV(cabecera,_id="calendario-cabezera")
        cal_tabla = DIV(tabla,_id="calendario-fechas")
        if request.vars['year']:
            if mes =="Enero":
                mes = DIV(cal_cabezera,cal_tabla,_id=mes,_class="esconder")
            else:
                mes = DIV(cal_cabezera,cal_tabla,_id=mes,_hidden = "true",_class="esconder")
        else:
            if meses.index(mes)==int(time.strftime("%m"))-1:
                mes = DIV(cal_cabezera,cal_tabla,_id=mes,_class="esconder")
            else:
                mes = DIV(cal_cabezera,cal_tabla,_id=mes,_hidden = "true",_class="esconder")
        calendario.append(mes)
    calendario = DIV(A("Anterior",_href=URL('reservaciones_existentes',vars=dict(year=str(int(year)-1)))),A("Siguiente",_href=URL('reservaciones_existentes',vars=dict(year=str(int(year)+1)))),calendario)
    return dict(calendario=calendario)
