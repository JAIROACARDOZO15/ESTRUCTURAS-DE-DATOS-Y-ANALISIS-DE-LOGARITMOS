# PROBLEMA
# Se tiene el registro con los datos de una transacción de un cliente a partir de un datafono en un archivo texto como lo son: numeros de tarjerta, valor de compra, codigo datafono y fecha; determinar el valor a cobrar por la comision del manejo de la transaccion de acuerdo a la siguiente tabla y generar las tuplas para los servicios de la transaccion:

# Rango comision
# 0-1000000 se le agrega 0.5%
# 100001 - 1000000  se le agrega 0.4%
#> 1000000 se le agrega 1%

# Como respuesta se debe generar dos tuplas, una para el establecimiento con los datos del codigo establecido (Diccionario de asignacion de datafonos), valor comision y neto a pagar. Otra para el banco del cliente con el numero de cuenta (Diccionario de asignacion de tarjetas) y el valor de la compra

import os
datafonos={1:"1015",2:"1025",3:"1035"}
tarjetas={1510:"830-25",1515:"830-35"}
archivo="D:/Mis documentos/Escritorio/ING SISTEMAS/ESTRU. DE DATOS Y ANALISIS DE LOGARITMOS/28-04-23 DUPLAS/transacciones.txt"
f=open(archivo,"r")
x=f.read()
lista=(x.split(","))
f.close()

valor=int(lista[1])
if valor>=0 and valor<=100000:
    comision=valor*0.5/100
if valor>100000 and valor<=1000000:
    comision=valor*0.4/100
if valor>1000000:
    comision=valor*1/100
neto=valor-comision

cod_est=datafonos[int(lista[2])]
tupla_Est=(cod_est,comision,neto)
print(tupla_Est)

cod_cuenta=tarjetas[int(lista[0])]
tupla_banco=(cod_cuenta,valor)
print(tupla_banco)