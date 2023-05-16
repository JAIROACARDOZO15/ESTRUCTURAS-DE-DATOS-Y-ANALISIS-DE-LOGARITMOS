# 1. Construir una sarta con cada una de las letras de mayor aparición en cada palabara de una frase digitadas por el usuario.

frase = input("Ingrese una frase: ")
lista = []
palabras = frase.split(" ")

for palabra in palabras:
    mas_repetidas = 0

    for letra in palabra:
        repetidas = palabra.count(letra)
        if repetidas > mas_repetidas:
            mas_repetidas = repetidas
    lista.append(letra)


print("La letra mas repetida en la frase ingresada es: ", lista)