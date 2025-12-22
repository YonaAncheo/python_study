print('hola mundo 2')
print('hola mundo')

for i in range(5):
    print(i)

for i in range(3):
    print(i*i)
    pass

# esto es un comentario

"""
esto es un 
comentario
multilinia
utilizando 3 comillas dobles
"""

# diccionario

dictionario: dict = {
    "juan": 1,
    "pedro": {"id":2,
              "dirección":"calle 2"},
    "diego":3
}

print(dictionario["juan"])
print(dictionario["pedro"]['dirección'])

texto = 'mayuscula'

mayuscula = texto.upper()

print(texto,mayuscula)

#manipular los espacios de un texto.

texto2 = '      muchos espacios              hola.   '

sin_espacios = texto2.strip()
print(sin_espacios)

# el método strip(), solo quita los espacios al principio y final.