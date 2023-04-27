#!/usr/bin/env python3
# Se tiene un archivo de texto plano en el que se almacenan los contenidos de un diccionario de español a inglés, las palabras se encuentran en el formato "español:ingles", el usuario ingresa una frase a traducir, la cuál es traducida teniendo en cuenta los significados dentro del archivo de texto.

# Se definen algunas variables necesarias para la ejecución del programa
diccionario = {}
archivo = open("archivo.txt", "r")
lineas = archivo.readlines()
palabra_desconocida = False
palabras_desconocidas = []

# Se recorren todas las lineas del archivo de texto
for linea in lineas:
    # Se separa la línea en las dos partes del diccionario
    palabras = linea.split(":")
    # Y se agrega al diccionario base
    diccionario[palabras[0]] = palabras[1][:-1]

# Se le pide al usuario que ingrese una frase a traducir
frase = input("Ingrese una frase a traducir: ")

# Se verifica si la frase ingresada es válida
while not frase:
    frase = input("Necesita escribir una frase a traducir: ")

# Se separa la frase ingresada en una lista de palabras
palabras = frase.split()
frase_traducida = ""

# Se recorren todas las palabras de la frase
for palabra in palabras:
    # Si la palabra está en el diccionario
    if palabra in diccionario:
        # Se agrega a la palabra traducida el significado de la palabra original
        frase_traducida += diccionario[palabra] + " "
    else:
        # Si no se encuentra en el diccionario se mantiene la palabra original
        frase_traducida += palabra + " "
        # Y se imprime cada palabra que no está en el diccionario
        print("La palabra " + palabra + " no está en el diccionario!")
# Se imprime la frase traducida al final
print(frase_traducida)
