def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n-1):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]
    return matriz

matriz = [[9, 5, 2],
          [4, 1, 7],
          [6, 3, 8]]

fila_a_ordenar = 1

print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

print("Matriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)