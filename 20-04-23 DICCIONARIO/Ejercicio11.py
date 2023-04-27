# Ejercicio - Diccionarios
#Desarrollar un programa que permita definir un grupo de diccionario para el sistema de ventas de una tienda, en donde el usuario digita el codigo del producto y la cantidad de vender, se debe generar el nombre del producto, el valor unitario,el valor total y saldo de inventario del producto. Al inicio de la facturacion se pregunta cuantos productos se van a registrar, al finalizar tambien se debe totalizar la factura

nombres={1:"Azucar",2:{"Pan"},3:{"Huevos"},4:{"Leche"}}
valores={1: 1800, 2: 1500, 3: 800, 4: 5000}
saldos={1:25, 2:5, 3:50, 4:15}

cantidad=int(input("Digite la cantidad de productos a facturar:"))
lista=[]
while cantidad<=0:
    print("Cantidad incorrecta, debe ser superior a 0")
    cantidad=int(input("Digite cantidad de productos a facturar: "))
total = 0
for i in range(cantidad):
    codigo=int(input("Digite código producto a facturar: "))
    while codigo not in nombres.keys():
        print("Codigo incorrecto")
        print(nombre)
        codigo=int(input("Digite el producto a facturar:"))
    can=int(input("Digite cantidad del producto a facturar:"))
    while can<=0:
        print("Cantidad incorrecta, debe ser superior a 0")
        can=int(input("Digite cantidad del procucto a facturar:"))
        
    x= saldos[codigo]
    y= valores[codigo]
    while can>x:
        print("Cantidad incorrecta, supera al saldo actual del producto, que es: ",x)
        can=int(input("Digite cantidad del producto a facturar: "))
    lista.append(str(codigo) + " - " + nombres[codigo] + " - " + str(can) + " - "+str(y) + " - "+str(can*y))
    total= total+ can * y
    saldos[codigo]=x-can

print("Factura de venta")
print("Codigo  Nombre  Cantidad  Vlr Unit  Vlr Total")
for i in lista:
    print(i)
print("------------------------------------")
print("Total Factura: ", total)