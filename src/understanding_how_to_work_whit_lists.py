# Trabajando con listas
"""
    Recorrer una lista sin impotar la cantidad
    de elementos que tenga.
"""

magicians = ["ron", "harry", "hermione", "hagrid", "cedric"]

print(magicians[0], magicians[1], magicians[2])

for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()}, ese fue un gran truco!")
    print(f"{magician.upper()} No podemos esoerar para ver tu proximo hechizo")

print("Gracias a todos, fue un gran espectaculo!")

"""
   Identacion:

   Python utiliza la identacion para determinar
   cuando una linea de codigo esta conectada a 
   la linea de codigo anterior.

   Basicamente, se utilizan 4 espacios en blanco
   para obligarnos a escribir codigo ordenado y
   estructurado
"""
# No olvidemos identar
# Error de logica
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)
print(f"I can't wait to see the next trick!, {magician.title()}")

# Identacion innecesaria
message = "Hello Python world!"
print(message)