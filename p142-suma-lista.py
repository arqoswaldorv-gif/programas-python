# p142-suma-lista.py
# Funcion para sumar los elemetnos de una lista de números

from typing import List
def suma_lista(lista:List[float]) -> int:
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Lista 1
lista = [1.5,2.3,3.7,4.0]
resultado = suma_lista(lista)
print('Suma 1 : ' , resultado)

# Lista 2
print('Suma 2 : ' , suma_lista ([1,5,6.5,7,8]))
