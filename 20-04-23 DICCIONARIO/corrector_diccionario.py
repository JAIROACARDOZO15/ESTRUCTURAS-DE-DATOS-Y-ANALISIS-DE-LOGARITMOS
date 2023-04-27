#!/usr/bin/env python3
# Generar un corrector ortográfico para una frase digitada por el usuario; las palabras de referencia se encuentran alamacenadas en un diccionario como la llave, las posibles palabras con incorrecciones se encuentran como una lista de valores para cada palabra de referencia. Para cada recomendación de cambio se le debe solicitar confirmación al usuario y posteriormente mostrar la nueva frase.

diccionario = {
    "hola": ["holla", "ola", "jola", "halo", "hol"],
    "mañana": ["manana", "maana", "majana", "nanana"],
    "vieja": ["viega", "bieja", "biega"],
    "estaba": ["estava", "hestava", "hestaba"],
    "corazón": ["corazon", "corason", "coason"],
}

frase = input("Ingrese una frase que desee: ")

palabras = frase.split()

indice = 0

for palabra in palabras:
    for value in diccionario.values():
        for error in value:
            if error == palabra:
                palabra_corregida = str(
                    list(diccionario.keys())[list(diccionario.values()).index(value)]
                )
                correccion = input(
                    "La palabra es "
                    + str(error)
                    + " tiene los siguientes errores, corregirlas por "
                    + palabra_corregida
                    + "? "
                    + "(si o no) "
                )
                if correccion == "si":
                    palabras[indice] = palabra_corregida            
    indice += 1
print(*palabras)
