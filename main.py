from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():

    restaurante = Restaurante()

    
    platillo1 = Platillo(
        "Hamburguesa Clásica",
        6.50,
        True,
        "Comida rápida"
    )

    platillo2 = Platillo(
        "Encebollado",
        4.75,
        True,
        "Mariscos"
    )

    
    bebida1 = Bebida(
        "Coca Cola",
        1.50,
        True,
        500
    )

    bebida2 = Bebida(
        "Jugo Natural",
        2.25,
        True,
        350
    )

    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)

    restaurante.mostrar_productos()

    print("Cambio de precio de la Coca Cola")
    bebida1.cambiar_precio(1.75)

    print("\nPrecio actualizado:")
    bebida1.mostrar_informacion()


if __name__ == "__main__":
    main()
