# open(nombre, mondo) es uno de los metodos para abrir archivos, y close() para cerrar
# la desventaja es que se debe abrir y cerrar, pero con with, se manipula de mejor manera

# R lectura
# W escritura
# X crear archivo

f = open('./fundamentos_python/archivo.txt','r')
print(f.readline())
f.close()

try:
    with open('./fundamentos_python/archivo.txt', 'r') as f:
        print(f.readline())
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    print('error')