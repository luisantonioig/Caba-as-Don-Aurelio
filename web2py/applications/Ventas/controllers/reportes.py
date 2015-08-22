def index(): return dict(message="hello from reportes.py")

def frecuencia():
    clientes= db().select(db.cliente.nombre)
    for cliente in clientes:
        print cliente.nombre
    veces_anuales= [10,21]
    return dict(clientes=clientes, veces_anuales=veces_anuales)

def calcular_frecuencia_visita(id):
    reservaciones = db(db.reservacion.cliente==id).select(db.reservacion.fecha_inicio,db.reservacion.fecha_fin)
    return 5
