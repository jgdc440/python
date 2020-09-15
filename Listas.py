list_a = [x ** 2 for x in range(10)]
list_b = list(map(lambda x: x**2, range(10)))

list_c = [-4, -2, 0, 2, 4]

positivos_I = [x for x in list_c if x >= 0]
positivos_II = list(filter(lambda x: x >=0, list_c))

print(positivos_I)
print(positivos_II)

pares_cuadrados = [(x, x ** 2) for x in range(6)]
print(pares_cuadrados)

pares_combinados = [(x,y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(pares_combinados)

combinados = [(x,y) for x in ['H1', 'H2', 'H3'] for y in ['M1', 'M2', 'M3', 'M4']]
a = len(combinados)
print(a)


tarea = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tarea = tarea[1:8]
tarea.append(9)
tarea.insert(0,5)
tarea.remove(5)
tarea.pop(0)
print(tarea)

pares = [x for x in range(101) if x % 2 == 0]
print(pares)

cuadrados = []
for x in range(10):
   cuadrados.append(x**2)
print(cuadrados)


list_d = [1, 2, 3, 4]
sorted(list_d, reverse=True)
print(list_d)
a = list_d.index(3, 2, 3)
print(a)

list_e = [(1,4), (1,1), (1,5), (1,2), (1,6),(1,2), (1,3)]
list_e.sort(key=lambda x: x[1])
print(list_e)

list_f = [(6,2),(1,5),(2,3),(4,1),(5,2),(1,3)]
list_f.sort(key=lambda x: x[0]+x[1])
print(list_f)

list_d = [1, 2, 3, 4]
list_d.sort(reverse=True)
print(list_d)

list_d = [1, 2, 3, 4]
list_d = sorted(list_d, reverse=True)
print(sorted(list_d, reverse=True))
print(list_d)

a = set('abracadra')
print(a)