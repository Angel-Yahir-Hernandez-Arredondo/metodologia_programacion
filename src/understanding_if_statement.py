cars = ["audi", "bmw", "chevrolet", "corvette", "tesla"]

for car in cars:
    if car == "bmw" or car == "tesla" or car == "audi":
        print(car.upper())
    else:
        print(car)
print("\n----Concicionales----")
# Condicionales: El condicional es el corazon de un if
# Condicional verdadero
car = "bmw"
print(car == "bmw")

# Condicional falso
car_2 = "Audi"
print(car_2 == "audi")

# Solucion al condicional falso
car_2 = "Audi"
print(car_2.lower() == "audi") # Salida -> True

# Condicional != para determinar desigualdad

requested_topping = "mushrooms" # -> string
if requested_topping != "anchovies":
    print("Hold the anchovies!")

# Comparaciones numericas
age = 18 # -> int
print(age == 18) # -> True
print(age != 18) # -> False

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)  # -> True
print(age <= 21) # -> True
print(age > 21)  # -> False
print(age >= 21) # -> False

# Mutiples condiciones
age_0 = 22
age_1 = 18
print("\n----Mutiples condiciones----")
print("Operacion and - PSeInt: Y")
print( age_0 >=21 and age_1 >=21 ) # -> False
print( age_0 >=21 and age_1 >=18 )  # -> True
print("\nOperacion or - PSeInt: O")
print( age_0 >=21 or age_1 >=21 )  # -> True
print( age_0 >=23 or age_1 >=21 )   # -> False

# ¿Cómo verificar si un valor está en una lista?
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('\n----Verificar si un valor está en una lista----')
print('mushrooms' in requested_toppings)  # -> True
print('pepperoni' in requested_toppings)  # -> False

# A value not in list
banned_users = ['gabriel', 'max', 'andrik', 'quevedo', 'christopher']
user = 'pedro'
print(user not in banned_users)  # -> True

# Variables de tipo booleano
game_active = True
can_edit = False

"""
   If statements

   If condition:
      do something
   
   If condition:
      do something(true)
   Else:
      do something(false)
"""
# Vamos a preguntar la edad del usuario y decirle si tiene la edad suficiente para votar
# input("") siempre regresa un string

# Solucion 1
age = int(input("\n\nEscribe tu edad:"))
print(f"\nTu edad es: {age}")
if int(age) >= 18:
    print("Tienes la edad suficiente para votar.")
else:
    print("No tienes la edad suficiente para votar.")

# Solucion 2
age = int(input("\n\nEscribe tu edad:"))
print(f"\nTu edad es: {age}")

if age >= 18:
    print("Tienes la edad suficiente para votar.")
else:
    print("No tienes la edad suficiente para votar.")