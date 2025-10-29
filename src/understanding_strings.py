"""

Strings variables

Un string es de manera sencilla una serie de caracteres.
En python, todo lo que se encuentre entre comillas simples ('...') o dobles ("...")
sera considerado un string.

Ejemplos:
    "Este es un string"
    'Este tambien es un string'

' Le dije a un amigo "Python es mi lenguaje favorito" '
" Le dije a un amigo 'Python es mi lenguaje favorito' "

"""
name = "clase de programacion"
print(name)


# title
print(name.title())

print(name)

"""
Un metodo es una accion que python puede realizar en un fragmento de datos o sobre una variable.


  El punto despues de una variable seguido del metodo title() dice que se tiene que ejecuar el metodo title()
sobre la variable name.

  Todos los metodos van seguidos de parentesis () porque en ocasiones necesitan informacion 
adicional para funcionar, la cual iria dentro de los parentesis. En esta ocasion el metodo title() no necesita 
informacion adicional para funcionar,
"""

print(" Metodo upper: ", name.upper())
print(" Metodo upper: ", name.lower())



# Concatenacion de strings
first_name = "charly"
last_name = "mercury"

full_name = first_name + " " + last_name
print(" Nombre completo: ", full_name)
print(full_name.title())
