"""
squeares=[]
for value in range(0, 11):
    squeare = value**2
    squeares.append(squeare)
print(squeares)
"""
"""
   Una list comprehension combina el ciclo for
   y la creacion de nuevos elementos en una sola linea, 
   y automaticamente agrega los nuevos elementos a la lista,
   es decir, sin utilizar el metodo append().
"""
squeares = [value**2 for value in range(0, 11)]
print("\n"squeares)
evens_range = [value for value in range(0, 101, 2)]
print("\n",evens_range)
evens_if = [value for value in range(0, 101) if value%2 == 0]
print("\n",evens_if)