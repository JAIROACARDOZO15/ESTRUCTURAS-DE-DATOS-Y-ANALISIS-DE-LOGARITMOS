#!/usr/bin/env python3
# Buscar una palabra o un patrón especifico en un archivo de texto plano (.txt)
# Importa los módulos necesarios para la ejecución
from time import perf_counter

# Pedir el input de la palabra por buscar
palabra = input("Ingrese una palabra para buscar: ")

# Empieza a tomar el tiempo de ejecución
inicio = perf_counter()

# Define las variables necesarias para realizar la comparación de cada letra
archivo = open("archivo_de_ejemplo.txt", "r")
duracion = len(archivo.read())
archivo.seek(0)
bandera = False

# Crea un foor loop anidado (n^2) en el que recorre todas las letras dentro del archivo y las compara con los diferentes caracteres de la palabra
for intento in range(duracion):
    # Empieza con el primer caracter de la palabra, y se reinicia si no se ha encontrado
    adivinado = 0
    # Por cada letra dentro del archivo de texto
    for letra in archivo.read():
        # Se compara si la letra iterada es igual al primer digito de la palabra
        if letra == palabra[adivinado]:
            # Si lo es le suma uno a la variable contador
            adivinado += 1
            # Si el contador es igual a la longitud de la palabra
            if adivinado == len(palabra):
                # Se reinicia el contador para no quedar por fuera del indice
                adivinado = 0
                # Se cambia el valor de la bandera para indicar el estado exitoso
                bandera = True
                # Se rompe el último ciclo for para continuar con la ejecución
                break
# Dependiendo del estado final de la bandera se imprime el resultado indicado
if bandera:
    print("SÍ se encontró la palabra!")
else:
    print("NO se encontró la palabra!")