def suma_matrices(A, B):

    cant_filas = len(A)
    cant_columnas = len(A[0])

    c = []

    for fila in range(cant_filas):
        fila_suma = []
        for col in range(cant_columnas):
            fila_suma.append(A[fila][col]-B[fila][col])
        c.append(fila_suma)
    return c


a = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
b = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

c = suma_matrices(a,b)
print(c)
