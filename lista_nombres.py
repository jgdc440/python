# Lista para ejercitar el acceso a los nombres 
# Métodos utilizados en las estructuras de datos de tipo lista
#
names = ['Jose', 'Ana', 'Carlos', 'Jesus', 'Victoria', 'Javier', 'Noraima', 'Marcela']

def acceder_nombre(index):
    
    if index == 0 or index == 2 or index == 3 or index == 5:
        message = "Querido " + names[index].title() + " está cordialmente invitado a mi cena el 24/06/2018"
    else:
        message = "Querida " + names[index].title() + " está cordialmente invitada a mi cena el 24/06/2018"
    return message

for i in range(len(names)):
    print(acceder_nombre(i))
    print()

print(acceder_nombre(-1)) # Muestro el último
print()
names[3] = "Wakanda" # Incluyo un elemento por su índice
print(names)
print()
names.append("Thor") # Incluyo un elemento por el método append
print(names)
print()
names.insert(1, "Spiderman") # Incluyo un elemento por el método insert en la posición deseada
print(names)
print()
del names[0] # Elimino un elemento por el método del en la posición que deseo
print(names)
print()
popped_names = names.pop() # Remuevo el último elemento de mi lista y lo conservo
print(names)
print()
print("The last friend what I have was " + popped_names + ".")
print()
nro_names = len(names) # Determino la longitud de mi lista
print("La lista tiene " +str(nro_names) +" elementos.") 
print()
popped_names = names.pop(0) # Remuevo el elemento de mi lista en la posición que deseo y lo conservo
print(names) # En este caso fue el primero, pero puedo extraer el que desee en cualquier posición
print()
print("The first friend what I have was " + popped_names + ".")
print()
names.remove("Carlos") # Remuevo elementos por su valor con el método remove. Solo remueve la primera coincidencia
print(names)
print()
nro_names = len(names) # Determino la longitud de mi lista
print("La lista tiene " +str(nro_names) +" elementos.") 
print()

for i in range(len(names)): # Acá se nos presenta un problema porque no sabemos el sexo de los invitados. Se puede resolver con un dictionary
    print(acceder_nombre(i)) 
    print()