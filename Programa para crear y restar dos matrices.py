# Programa para crear y restar dos matrices cuadradas

# Solicitar dimensiones de las matrices
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Crear la primera matriz
print("Ingresando valores para la primera matriz:")
matriz1 = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese valor para: ({i}, {j}) "))
        fila.append(valor)
    matriz1.append(fila)

print(matriz1)

# Crear la segunda matriz
print("Ingresando valores para la segunda matriz:")
matriz2 = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese valor para: ({i}, {j}) "))
        fila.append(valor)
    matriz2.append(fila)

print(matriz2)

# Calcular la resta de matrices (matriz1 - matriz2)
print("Resultado de resta")
resultado = []
for i in range(filas):
    fila_resultado = []
    for j in range(columnas):
        resta = matriz1[i][j] - matriz2[i][j]
        fila_resultado.append(resta)
    resultado.append(fila_resultado)

print(resultado)