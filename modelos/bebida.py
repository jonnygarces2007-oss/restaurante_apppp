from modelos.producto import Producto


class Bebida(Producto):
    
    def __init__(self, nombre, precio, disponible, volumen_ml):
        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml

    
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        print(f"""
----- BEBIDA -----
Nombre: {self.nombre}
Volumen: {self.volumen_ml} ml
Precio: ${self.obtener_precio()}
Estado: {estado}
""")
