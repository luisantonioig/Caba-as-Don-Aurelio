def index(): return dict(message="hello from reportes.py")

def frecuencia():
    clientes= db(db.cliente.nombre)
    return dict(clientes=clientes)
