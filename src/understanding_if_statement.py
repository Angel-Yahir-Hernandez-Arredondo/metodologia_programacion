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

# Condicional falso
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

