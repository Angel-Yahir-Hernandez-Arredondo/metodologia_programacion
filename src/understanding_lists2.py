"""
   Slicing a list
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Lista original: ", players)

print("\nSlice de lista orginal: ", players[0:3])
print("\nSlice de lista orginal: ", players[1:4])
print("\nSlice de lista orginal: ", players[:4])
print("\nSlice de lista orginal: ", players[2:])
print("\nSlice de lista orginal: ", players[-3:])
print("\nSlice de lista orginal: ", players[4:2])
print("\nSlice de lista orginal: ", players[-3:-1])

"""
   Slicing en un for
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Aqui se presentan los 3 primeros jugadores del equipo")
for player in players[0:3]:
    print(player.title())

"""
   Copiando una lista
"""
my_foods = ['pizza', 'tacos', 'flautas', 'gorditas']
my_foods_copy = my_foods #Error: esta no es la manera de copiar listas
my_foods_1 = my_foods[:] #Forma 1 de copiar
my_foods_2 = my_foods.copy()
my_foods_3 = list(my_foods)