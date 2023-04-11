lista = []

while True:
    menu = input(
        "1. Agregar un elemento\n2. Mostrar la lista actual\n3. Eliminar el último elemento\n4. Contar las veces que un elemento está en la lista\n5. Salir\n"
    )

    if menu == "1":
        elemento = input("Digite un número para agregar: ")
        lista.append(elemento)
    elif menu == "2":
        print(lista)
    elif menu == "3":
        lista.pop()
    elif menu == "4":
        elemento = input("Digite un número para contar: ")
        print(lista.count(elemento))
    elif menu == "5":
        break