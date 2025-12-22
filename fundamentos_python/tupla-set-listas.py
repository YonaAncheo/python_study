print(mi_lista:= [1, 'list', True], type(mi_lista))
print(mi_set:= {2,3,'conjunto', 'conjunto', False}, type(mi_set))
print(mi_tupla:= (3, 'tupla', True),type(mi_tupla))

# podemos obtener una tupla modificada utilizando un lista comodin y casteando

lista_comodin: list = list(mi_tupla)
lista_comodin.remove('tupla')
lista_comodin.append("esto")
lista_comodin.append("esto")
lista_comodin.append("es")
lista_comodin.append("una")
lista_comodin.append("prueba")
lista_comodin.append(True)

print(lista_comodin, type(lista_comodin))
print(nueva_tupla := tuple(lista_comodin), type(nueva_tupla))
print(nueva_set := set(lista_comodin), type(nueva_set))

# metodos conjuntos.

print(conjunto_union := nueva_set.union(mi_set), "# union")
print(conjunto_inter := nueva_set.intersection(mi_set), "# intesección")
print(conjunto_diff := nueva_set.difference(mi_set), "# diferencia")

''''
[1, 'list', True] <class 'list'>
{False, 'conjunto', 2, 3} <class 'set'>
(3, 'tupla', True) <class 'tuple'>
[3, True, 'esto', 'esto', 'es', 'una', 'prueba', True] <class 'list'>
(3, True, 'esto', 'esto', 'es', 'una', 'prueba', True) <class 'tuple'>
{True, 'esto', 3, 'prueba', 'una', 'es'} <class 'set'>
{False, True, 2, 'esto', 3, 'prueba', 'una', 'conjunto', 'es'} # union
{3} # intesección
{True, 'esto', 'prueba', 'una', 'es'} # diferencia
'''

