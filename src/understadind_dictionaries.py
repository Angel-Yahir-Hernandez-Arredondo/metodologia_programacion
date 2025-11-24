# Empty Dictionary
homer_0 = {
    'color': 'yellow',
    'bag': 'maggie-bag',
    'hair': 'black',
    'dress': 'blue', 
    'mom': False
}
print(homer_0)
print(type(homer_0))

marge={
    "color": "yellow", 
    'bag': 'homer_donut', 
    'hair': 'blue', 
    'dress': 'green', 
    'mom': True}
gun_0={'scar': 'yellow_orange', 'headshot': 1.5}

## Add elements to a dictionary

print(homer_0)
homer_0["x-position"]=15
homer_0["y-position"]=25
homer_0["z-position"]=10
print(homer_0)

marge["x-position"]=16
marge["y-position"]=26
marge["z-position"]=10

alien_0={'color': 'yellow'}
print(alien_0['color'])

# Modifying values in a dictionary
alien_0['color']='green'
print(alien_0['color'])

# Add elements to a dictionary
alien_0['x-positions']=0
alien_0['y-positions']=0
alien_0['name']='Paul'

print(alien_0)

##Looping though items
for key, value in alien_0.items():
    print(f"\nKey: {key} has value: {value}")

##Looping though keys
for key in alien_0.keys():
    print(f"\nKey: {key}")

##Looping though values
for value in alien_0.values():
    print(f"\nValue: {value}")

# NESTING
# Listas de diccionarios
# Listas en diccionario
# Diccionarios en diccionarios