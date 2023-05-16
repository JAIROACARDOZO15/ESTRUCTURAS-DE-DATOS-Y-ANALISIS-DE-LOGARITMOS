palabra = "supercalifragilisticoespialidoso"

# Encontrar las letras únicas en la palabra
letras_unicas = set(palabra)

# Inicializar una variable para el número máximo de repeticiones
max_repeticiones = 0

# Inicializar una variable para la letra más repetida
letra_mas_repetida = ''

# Iterar sobre cada letra única en la palabra
for letra in letras_unicas:
    # Contar cuántas veces aparece la letra en la palabra
    repeticiones = palabra.count(letra)
    
    # Si la letra tiene más repeticiones que las encontradas hasta ahora
    # actualizar la letra más repetida y el número máximo de repeticiones
    if repeticiones > max_repeticiones:
        max_repeticiones = repeticiones
        letra_mas_repetida = letra

# Imprimir la letra más repetida
print("La letra más repetida en la palabra es:", letra_mas_repetida)