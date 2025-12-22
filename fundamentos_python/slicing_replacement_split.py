#slicing, nos permite manejar que partes del texto se usarán

texto = 'Esto es un texto'

print(texto[5:-2])
print(texto[:8])
print(texto[8:])

# con replace podemos reemplazar todas las veces que se repita una palabra en un texto
curso = 'Este curso es de JavaScript.'

print(curso.replace('JavaScript','Python'))

# el método split(), nos permite separar los textos en listas de las palabras
print(type(curso.split()),":",curso.split())