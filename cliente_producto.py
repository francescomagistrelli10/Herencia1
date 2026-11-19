class Cliente:
    def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad
    def __init__(self, nombre, email, edad,telefono):
            self.nombre = nombre
            self.email = email
            self.edad = edad 
            self.telefono = telefono

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

def compra(cliente, producto, unidades):
    total = producto.precio * unidades
    print(f"{cliente.nombre} ha comprado {unidades} unidades de {producto.nombre} por un total de {total}.")

