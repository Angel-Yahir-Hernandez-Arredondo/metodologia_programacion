"""
   Las listas son elementos mutables.

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