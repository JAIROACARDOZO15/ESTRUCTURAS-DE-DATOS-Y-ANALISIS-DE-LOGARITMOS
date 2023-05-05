corrections = {
    "hola": ["holla", "hela", "holi", "hula"],
    "mundo": ["mundi", "munda", "mundu", "mundo"],
    "mañana": ["manana", "nañana"]
}
errors = {}
for key, values in corrections.items():
    for value in values:
        errors[value] = key

frase = input("Escribe una frase: ")

palabras = frase.split()
for i in range(len(palabras)):
    palabra = palabras[i]
    correccion = errors.get(palabra)
    if correccion is not None:
        print(f"La palabra '{palabra}' está mal escrita. La posible corrección es '{correccion}'")
        respuesta = input("¿Quieres corregirla? (S/N): ")
        if respuesta.upper() == "S":
            palabras[i] = correccion

nueva_frase = " ".join(palabras)


print(f"La frase corregida es: {nueva_frase}")


