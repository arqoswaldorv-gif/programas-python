# p143-lista-pares.py
# Funcion que recibe una lista de numeros enteros y regresa una lista de lso apres

from typing import List

def lista_pares(lista: List[int]) -> List[int]:
    pares : List[int] = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# Lista 1
numeros : List[int] = [1,2,3,4,5,6,7,8,9,10,12]
resultado : List[int] = lista_pares(numeros)
print(f'Lista de numeros pares : {resultado}')

# Lista 2
print(f'Lista de numeros pares : {lista_pares( [20,45,67,89,12,22] ) }')

# Lista 3
print(f'Lista de numeros pares : {lista_pares( [1,3,5,7,8] ) }')