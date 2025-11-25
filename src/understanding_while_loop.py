# While
"""
   El while es un ciclo controlado/comandado
   por una condicion.

   La estrucutra basica de un while es:

      while conditional:
        actions
"""

# While infinito
"""
    Programa si el usuario escribe un numero entre 25 y 50,
    entonces estar dentro del rango y salirme del while,
    de otro modo pedirle otro numero.
"""
while True:
    try:
        number= int(input("Ingresa un numero: "))

        if number >=25 and number <=50:
            print("El numero esta dentro del rango")
            break
        else:
            print("El numero esta fuera del rango, intenta de nuevo")
    
    except ValueError:
        print("Caracter no valido")