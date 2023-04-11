# Crear un programa con el siguiente menú de opciones para la administración de una lista de números
# 1. Agregar Elemento
# 2. Mostrar lista actual
# 3. Eliminar el ultimo Elemento
# 4. Contar las veces que un elemento está en la lista
# 5. Salir

lista_numeros = []
def agregar_elemento():
    num = int(input("Ingrese el número a agregar: "))
    lista_numeros.append(num)

def mostrar_lista():
    if not lista_numeros:
        print("La lista está vacía")
    else:
        print("Lista actual:", lista_numeros)

def eliminar_ultimo_elemento():
    if not lista_numeros:
        print("La lista está vacía")
    else:
        lista_numeros.pop()
        print("El último elemento ha sido eliminado")

def contar_elemento():
    if not lista_numeros:
        print("La lista está vacía")
    else:
        num = int(input("Ingrese el número a contar: "))
        veces = lista_numeros.count(num)
        print("El número", num, "aparece", veces, "veces en la lista")

def salir():
    print("¡CHAO !")
    exit()

menu = {
    1: agregar_elemento,
    2: mostrar_lista,
    3: eliminar_ultimo_elemento,
    4: contar_elemento,
    5: salir
}
while True:
    print("""
--- MENÚ DE OPCIONES ---
1. Agregar Elemento
2. Mostrar lista actual
3. Eliminar el ultimo Elemento
4. Contar las veces que un elemento está en la lista
5. Salir
""")
    opcion = int(input("Ingrese una opción: "))

    if opcion in menu:
        menu[opcion]()
    else:
        print("Opción no válida, intente nuevamente")