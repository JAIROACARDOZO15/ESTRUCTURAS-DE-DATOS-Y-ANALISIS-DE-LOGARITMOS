#!/usr/bin/env python3
# Desarrollar un programa que permita definir un grupo de diccionarios para el sistema de ventas de una tienda, en donde el usuario digita el código del producto y la cantidad a vender, se debe generar el nombre del producto, el valor unitario, el valor total y descontar el saldo de inventario del producto. Al inicio de la facturación se pregunta cuántos productos se van a registrar, al finalizar también se debe totalizar la factura.

# Se define el diccionario base con todos las propiedades de los productos
productos = [
    {"001": "Papas", "002": "Mango", "003": "Guayabas"},
    {"001": 500, "002": 600, "003": 800},
    {"001": 5, "002": 3, "003": 6},
]
# Se crea una lista para mostrar todos los datos de la factura
factura = []

# Inicia la facturación
# Se le preguntan al usuario los diferentes datos para generar la factura
cantidad_venta = int(input("Ingrese la cantidad de productos a comprar en total: "))
# Se valida que la cantidad de productos a comprar sea mayor de cero
while cantidad_venta <= 0:
    print("La cantidad de productos a comprar en total no es válida!")
    cantidad_venta = 0
    cantidad_venta = int(input("Ingrese la cantidad de productos a comprar en total: "))

costo_total = 0
for producto in range(cantidad_venta):
    codigo_producto = input("Ingrese el código del producto: ")
    # Se comprueba que el código del producto se encuentre en el diccionario base
    while codigo_producto not in productos[0].keys():
        print("El código del producto ingresado no existe!")
        print(productos[0])
        codigo_producto = ""
        codigo_producto = input("Ingrese el código del producto: ")
    cantidad_productos = int(
        input("Ingrese la cantidad de productos que va a registar: ")
    )
    # Se comprueba que la cantidad del producto a comprar no sea mayor que el saldo
    while cantidad_productos > productos[2][codigo_producto]:
        print(
            "La cantidad del producto a comprar es mayor que el saldo actual de la tienda!"
        )
        cantidad_productos = 0
        cantidad_productos = int(
            input("Ingrese la cantidad de productos que va a registar: ")
        )
    # Se definen variables con las diferentes consultas al diccionario para optimizar
    costo_prod = productos[1][codigo_producto]
    costo_total += costo_prod * cantidad_productos
    # Se agregan los distintos valores a la factura para imprimirlos
    factura.append(
        "x"
        + str(cantidad_productos)
        + " "
        + productos[0][codigo_producto]
        + " - $"
        + str(costo_prod)
        + " c/u - $"
        + str(costo_prod * cantidad_productos)
    )
    # Se descuenta el saldo de la tienda dependiendo de la cantidad de productos que se venden
    productos[2][codigo_producto] -= cantidad_productos
# Se imprime la factura en pantalla
print("\nFACTURA DE VENTA")
print("--------------------------------")
for producto in factura:
    print(producto)
print("--------------------------------")
print("TOTAL: $" + str(costo_total))
