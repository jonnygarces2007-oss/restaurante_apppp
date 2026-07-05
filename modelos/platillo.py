from modelos.producto import Producto


class Platillo(Producto):
   

    def __init__(self, nombre, precio, disponible, tipo_platillo):
        super().__init__(nombre, precio, disponible)
        self.tipo_platillo = tipo_platillo

   
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        print(f"""
----- PLATILLO -----
Nombre: {self.nombre}
Tipo: {self.tipo_platillo}
Precio: ${self.obtener_precio()}
Estado: {estado}
""")
