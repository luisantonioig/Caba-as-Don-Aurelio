# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from cliente.py")

def nuevo():
    formulario = SQLFORM(db.cliente)
    return dict(Nuevo_cliente = formulario)

def ver_clientes():
    grid = SQLFORM.grid(db.cliente)
    return dict(grid=grid)
