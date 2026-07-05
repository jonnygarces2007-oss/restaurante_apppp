# restaurante_apppp
# Sistema Restaurante - Programación Orientada a Objetos

## Estudiante

Jonny Javier Garcés Almeida

## Descripción

Este proyecto implementa un sistema sencillo para administrar productos de un restaurante utilizando Programación Orientada a Objetos en Python.

## Estructura

```
restaurante_app/
│
├── modelos/
├── servicios/
└── main.py
```

## Herencia

Se implementó una clase padre llamada **Producto** y dos clases hijas:

- Platillo
- Bebida

Las clases hijas reutilizan los atributos comunes mediante el uso de `super()`.

## Encapsulación

El atributo **precio** se encuentra encapsulado mediante `__precio`.

Su acceso se realiza utilizando:

- obtener_precio()
- cambiar_precio()

Además, el método cambiar_precio() valida que el nuevo precio sea mayor que cero.

## Polimorfismo

Las clases Platillo y Bebida sobrescriben el método:

```
mostrar_informacion()
```

Cuando la clase Restaurante recorre la lista de productos, cada objeto muestra su información de forma diferente dependiendo de su tipo.

## Reflexión

La Programación Orientada a Objetos permite desarrollar aplicaciones más organizadas, reutilizables y fáciles de mantener. El uso de herencia, encapsulación y polimorfismo facilita la creación de sistemas modulares que pueden ampliarse sin modificar gran parte del código existente.
