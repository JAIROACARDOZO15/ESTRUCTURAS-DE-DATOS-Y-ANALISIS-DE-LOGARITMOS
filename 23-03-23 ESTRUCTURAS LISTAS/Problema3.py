# Problema 3
# Una empresa tiene a la venra 5 productos diferentes con sus precios, elaborar un programa que le muestre al usuario el menú de productos (código, mobre, valor unitario) y permite facturar una venta (validar que máximo se puedan seleccionar 5 productos para la venta), se digita el código de un producto y la cantidad a comprar, se debe visualizar el total de la compra teniendo en cuenta agregar el 19% de iva. El programa debe validar que la digitación del producto sea correcta, es decr se encuentre en la lista. 

productos = []
productos.append([1, "A", 200])
productos.append([2, "B", 500])
productos.append([3, "C", 600])
productos.append([4, "D", 700])
productos.append([5, "E", 800])

n = int(input("Digite cantidad de productos: "))
while n>len(productos):
    print("Maximo 5 productos: ")
    n = int(input("Digite cantidad productos: "))
for i in range(n):
    cod=int(input("Digite código producto"))
    can=int(input("Digite cantidad producto"))