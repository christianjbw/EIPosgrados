#compresion de listas

#regular
letras = []
for i in "Python es el mejor lenguaje de programacion":
    letras.append(i)
print(letras)

#nueva forma
letras2 = [i for i in "Python es el mejor lenguaje de programacion"]
print(letras2)

#con condicional
pares = [i for i in range(1,21) if i%2==0]
print("Los numeros pares entre 1 y 21 son: ", pares)

#Funciones map, filter y reduce

#forma regular
elementos = [2, 3, 5, 4, 1, 3]
cuadrados = []

for i in elementos:
    cuadrados.append(i**2)

print("El cuadrado de la lista", elementos, "es", cuadrados)

#uso de map
def cuadrado(n):
    return n**2

cuadrados2 = list(map(cuadrado, elementos))

print("El cuadrado de la lista", elementos, "es", cuadrados2)

#uso de filter
def es_par(n):
    return n%2==0

numeros = list(range(1,21))

pares = list(filter(es_par, numeros))
print(pares)

#uso de reduce
from functools import reduce

def multiplica(m,n):
    return m*n

numeros = list(range(1,10))
producto = reduce(multiplica, numeros)

print("El producto de todos los elementos:", numeros, "es", producto)