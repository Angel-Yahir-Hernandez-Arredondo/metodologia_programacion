"""
   Las listas son elementos mutables.(Puede ser modificada)

   Las listas nos permiten almacenar informacion en un lugar,
   la cantidad que tengas: ya sean pocos elementos o millones
   de elementos.

   Se recomienda nombrar una variable de tipo lista en plural.

   En python, los corchetes [] definen una lista, sus elementos
   van separados por comas.
   Ejemplo:
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'giant']
print(bicycles)

print(bicycles[0])  # Primer elemento de la lista
print(bicycles[0].title())  # Primer elemento con la primera letra en mayuscula

# Los indices en python empiezan en 0 y terminan en n-1, donde n es el numero de elementos
print(bicycles[4].title())  # Quinto elemento de la lista

# Accediendo al ultimo elemento de la lista
print(bicycles[-1].title())  # Ultimo elemento de la lista
print(bicycles[-2].title())  # Penultimo elemento de la lista
print(bicycles[-5].title())  # Primer elemento de la lista

# Utilizando valores de la lista
message = "Mi primer bicicleta fue una " + bicycles[4].upper() + "."
print(message)
message_f = f"Mi primer bicicleta fue una {bicycles[4].title()}."
print(message_f)

## Agregar elementos a una lista
print("\n")
print("Agregar elementos a una lista")
print(bicycles)

print("Metodo de las listas para agregar elementos: list_name.append(element)")
bicycles.append('ducatti')
print(bicycles)

"""
    # Listas A-105
    Agregar elementos a una lista
      -append(): Agrega un elemento al final de la lista

"""
print("\n--- Agregar elementos a una lista metodo append() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducatti')
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki', 'ducatti']

"""
Agregar elementos a una lista en una posicion especifica
insert(): Agrega un elemento en la posicion especificada
"""
print("\n--- Agregar elementos a una lista metodo insert() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #Salida: ['honda ', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducatti') #Agrega 'ducatti' en la posicion 1
print(motorcycles) #Salida: ['honda', 'ducatti', 'yamaha', 'suzuki']

"""
      Eliminar elementos de una lista
         -del: Elimina un elemento en una posicion especifica
         -pop(): Elimina el ultimo elemento de la lista y lo devuelve
         -remove(): Elimina un elemento por su valor
"""
print("\n--- Eliminar elementos de una lista metodo del ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[0] #Elimina el elemento en la posicion 1
print(motorcycles) #Salida: ['yamaha', 'suzuki']

print("\n--- Eliminar elementos de una lista metodo pop() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop() #Elimina el ultimo elemento y lo guarda en una variable
print(motorcycles) #Salida: ['honda', 'yamaha']
print(f'La ultima motocicleta que borraste fue {popped_motorcycle}') #Salida: 'suzuki'

"""
   Eliminar un elemento por su valor
   pop(index): Elimina el elemento en la posicion especificada y lo devuelve
"""
print("\n--- Eliminar elementos de una lista metodo pop(index) ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0) #Elimina el elemento en la posicion 0 y lo guarda en una variable
print(f'La primera motocicleta que tuve fue una {first_owned}') #Salida: 'honda'
print(motorcycles) #Salida: ['yamaha', 'suzuki']

"""
   Eliminar un valor especifico de una lista por su valor
   remove(value): Elimina la primera aparicion del valor especificado
"""
print("\n--- Eliminar elementos de una lista metodo remove(value) ---") 
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducatti']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki', 'ducatti']
motorcycles.remove('ducatti') #Elimina 'ducatti' de la lista
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']

"""
    Organizar una lista
       -sort(): Ordena la lista de forma permanente en orden alfabetico
"""
print("\n--- Organizar una lista metodo sort() ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducatti']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki', 'ducatti']
motorcycles.sort() #Ordena la lista en orden alfabetico
print(motorcycles) #Salida: ['ducatti', 'honda', 'suzuki', 'yamaha']
print("\n")

motorcycles.sort(reverse=True) #Ordena la lista en orden alfabetico inverso
print(motorcycles) #Salida: ['yamaha', 'suzuki', 'honda', 'ducatti']