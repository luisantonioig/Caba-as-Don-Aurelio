def index(): return dict(message="hello from reportes.py")

def frecuencia():
    clientes= db().select(db.cliente.nombre,db.cliente.id)
    veces_anuales = []
    for cliente in clientes:
        print cliente.nombre
        veces_anuales.append(calcular_frecuencia_visita(cliente.id))
        print calcular_frecuencia_visita(cliente.id)
    return dict(clientes=clientes, veces_anuales=veces_anuales)

def calcular_frecuencia_visita(id):
    reservaciones = db(db.reservacion.cliente==id).select(db.reservacion.fecha_inicio,db.reservacion.fecha_fin)
    dias_totales=0
    for reservacion in reservaciones:
        dias_totales=dias_totales + abs((reservacion.fecha_inicio - reservacion.fecha_fin).days)
    return dias_totales
