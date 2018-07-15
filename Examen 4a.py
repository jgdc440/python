import math

a = [1, 2, 5, 4]

print sum(a)

b = ["This", "course", "is", "great"]
 
print len(b)

print b[3]

print b[1:3]


my_list = [0, 1, 2, 3, 4]
# Respuesta 2
a = my_list[0: len(my_list) // 2]
b = my_list[len(my_list) // 2 : len(my_list)]

print a , b

# Respuesta 3
a = my_list[: len(my_list) // 2]
b = my_list[len(my_list) // 2 :]

print a , b

def dist_points(p, q):
       return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
    

def dist_circ(p, q):
    radius = 2
    return abs(math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) - radius)

print "Distancia entre dos puntos", dist_points([4, 7], [2, 9]) 

print "Distancia de un punto al centro del circulo", dist_circ([4, 7], [2, 9]) 