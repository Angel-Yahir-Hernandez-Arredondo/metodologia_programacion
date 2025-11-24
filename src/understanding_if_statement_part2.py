age = 0
"""
try:
    age = int(input("Escribe tu edad: "))

except:
    age=-1
    print("Error: Ingresaste un caracter no valido")

#<>if-elif-else
if age>=100:
    print("Tienes mas de un siglo")
elif age>=18 and age<100:
    print("Tienes la edad para votar")
elif age>=0 and age<18:
    print("No puedes votar")
else:
    print("Tuviste un error")

print("Holi charly")
"""
"""
   Hacer un pregrama que pregunta la edad de una persona y responda lo siguiente
   -SI la edad es menor e igual a 4, entonces la entrada es gratuita
   -Si la edad es menor a 18, pero mayor que 4, entonces la entrada cuesta 200
   -Si la edad es mayor o igual que 18, entonces la entrada cuesta 400
"""
age_client=0
try:
    age_client = int(input("Escribe tu edad "))
except:
    age_client=-1
    print("Error, ingresaste un caracter no valido")

if age_client<=4 and age_client>=0:
    print("Tu entrada es gratuita")
elif age_client>4 and age_client<18:
    print("Tu entrada tiene un costo de $200")
elif age_client>18 and age_client<100:
    print("Tu entrada tiene un costo de $400")
elif age_client<0:
    print("Tuviste un error")
elif age_client>=100:
    print("Potencialmente muerto")

# Multiple if
guisos= ['asado','tamales','salsa verde']
if 'asado' in guisos:
    print('Si hay asado')
else:
    print('No hay asado')
if 'sopes' in guisos:
    print('Si hay sopes')
else:
    print('No hay sopes')
if 'salsa verde' in guisos:
    print('Si hay salsa verde')
else:
    print('No hay salsa verde')

#Lista vacia
guisos = []
if guisos:
    print('Hay guisos')
else:
    print('No hay guisos')

# Utilizando varias listas
guisos_disponibles=["salsa verde", "deshebrada", "mole", "caldo de iguana"]
guisos_a_ordenar=["deshebrada", "caldo de iguana"]
print('¿Qué guiso desea ordenar?')
for guiso in guisos_a_ordenar:
    print(f'Deseo {guiso}')
    if guiso in guisos_disponibles:
        print(f'Si tenemos {guiso}')
    else:
        print('No tenemos de ese guiso')
print('Realizando pedido...')