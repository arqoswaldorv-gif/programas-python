# p146-pares-impares.py
# Funcion que regresa lso apres e impares de una lsita

from typing import List, Tuple
def lista_pares_impares(lista:List[int]) -> Tuple[List[int], List[int] ]:
    pares : List[int] = []
    impares : List[int] = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

numeros : List[int] = [1,2,3,4,5,6,7,8,9,10,11,12]
pares, impares = lista_pares_impares(numeros)

print(f'Lista numeros {numeros} - {len(numeros)}')
print(f'Lista pares {pares} - {len(pares)}')
print(f'Lista impares {impares} - {len(impares)}')