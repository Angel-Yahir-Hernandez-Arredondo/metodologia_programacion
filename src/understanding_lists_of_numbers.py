"""
   Las listas tambien pueden almacenar numeros
   y de hecho, son ideales para esto.
   Python ofrece una gran cantidad de herramientas
   que ayudan a trabajar eficazmente con listas de numeros.
"""
# Metodo build in range()
"""
   El metodo range() genera una serie de numeros.
   Por ejemplo:
"""
print("Numeros del 0 al 9:")
for value in range(10): # Genera numeros del 0 al 9
    print(value)

print("\nNumeros del 1 al 9:")
for value in range(1, 10): # Genera numeros del 1 al 9
    print(value)

print("\nNumeros impares del 1 al 9:")
for value in range(1, 10, 2): # Genera numeros impares del 1 al 9
    print(value)
odd_numbers = list(range(1, 10, 2))
print("\nLista de numeros impares del 1 al 9:", odd_numbers)


print("\nNumeros pares del 0 al 9:")
for value in range(0, 10, 2): # Genera numeros pares del 0 al 9
    print(value)
even_numbers = list(range(0, 10, 2))
print("\nLista de numeros pares del 0 al 9:", even_numbers)

print("\nTabla de multiplicar del 9:")
for value in range(0, 91, 9): # Genera la tabla de multiplicar del 9
    print(value)
multiples_of_nine = list(range(0, 91, 9))
print("\nLista de multiplos de 9 del 0 al 90:", multiples_of_nine)

# Cuadrados de los primeros 10 numeros
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print("\nCuadrados de los primeros 10 numeros:", squares)

## Mas metodos build in
# Metodo min()
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # Salida: 0
# Metodo max()
print(max(digits))  # Salida: 9
# Metodo sum()
print(sum(digits))  # Salida: 45