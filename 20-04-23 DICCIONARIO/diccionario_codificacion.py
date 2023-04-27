#!/usr/bin/env python3
# Se tiene un diccionario incial con 5 palabras codificadas con números del 1 al 5, el usuario digita un grupo indeterminado de palabras, las cuáles deben ser codificadas en un solo código númerico. Si la palabra no existe en el diccionario, se debe agregar al mismo y su código sería el número siguiente al último código registrado en el diccionario.

# Se crea un diccionario base
diccionario = {1: "hola", 2: "buenas", 3: "noches", 4: "todos"}

# Se pregunta la frase y se separa en palabras
frase = input("Ingrese la frase que desee: ")
frase = frase.split()
frase_codificada = ""

# Recorre todas las palabras de la frase
for palabra in frase:
    codificado = False
    # Recorre todos los valores del diccionario
    for valor in diccionario.values():
        # Si son iguales se codifica
        if valor == palabra:
            codificado = True
            frase_codificada += str(
                list(diccionario.keys())[list(diccionario.values()).index(valor)]
            )
    # Si la palabra no ha sido codificada entonces se agrega al diccionario
    if codificado == False:
        indice = int(list(diccionario)[-1])
        diccionario[indice + 1] = palabra
        frase_codificada += str(list(diccionario.keys())[indice])

# Se imprime en pantalla la palabra codificada
print(frase_codificada)
