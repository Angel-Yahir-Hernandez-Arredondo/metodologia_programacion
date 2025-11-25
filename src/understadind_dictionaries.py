# Empty Dictionary
'''
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
'''
# NESTING
# Listas de diccionarios
# Listas en diccionario
# Diccionarios en diccionarios

covenant_grunt = {
    "color": "orange",
    "weapon": "plasma_gun",
    "armament": "plasma-grenade",
    "health": 2,
}

covenant_elite = {
    "color": "blue",
    "weapon": "plasma-sword",
    "armament": "plasma-grenade",
    "health": 7,
}

covenant_jackal = {
    "color": "gray",
    "weapon": "plasma-gun",
    "armament": "plasma-grenade",
    "health": 5,
}

covenants = [
    covenant_grunt,
    covenant_elite,
    covenant_jackal
]

for covenant in covenants:
    print("\n", covenant)
    for key, value in covenant.items():
        print(f"{key}: {value}")

# Listas en diccionarios
students = {
    "santiago": ['reprobado', 'prepa1', 'rebelde'],
    "jorge": ['aprobado', 'cbtis271', 'goleador'],
    "gabriel": ['aprobado', '119muerte', 'fornite'],

}

# Diccionarios en diccionarios
sensores= {
    'temperatura': {
        'id': 'temp_1',
        'location': 'aula 105',
        'value': 25,
        'unit': 'Celsius',
    },
    'humedad': {
        'id': 'hum_1',
        'location': 'aula 103',
        'value': 60,
        'unit': 'Porcentaje',
    }
}

print("Temperatura:")
print(sensores['temperatura']['value'])
print("Ubicacion:")
print(sensores['temperatura']['location'])

# Metodo get()
