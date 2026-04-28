# p147-aleatorios.py
# Genera dos listas con numeros aleatorios y los suma en una tercera

import random
from typing import List

def genera_aletorios(n:int, min:int, max:int) -> List[int]:
    nums : List[int] = []
    for _ in range(n):
        num = random.randint(min,max)
        nums.append(num)
    return nums

def suma_lista(l1:List[int], l2:List[int]) -> List[int]:
    suma : List[int] = []
    for i in range(len(l1)):
        s = l1[i] + l2[i]
        suma.append(s)
    return suma
    
def main() -> None:
    MAX = 100
    lista1 : List[int] = genera_aletorios(MAX, 1, 100)
    lista2 : List[int] = genera_aletorios(MAX, 20, 40)
    lista3 : List[int] = suma_lista(lista1, lista2)

    print(f'Lista 1: {lista1} - {len(lista1)}')
    print(f'Lista 2: {lista2} - {len(lista2)}')
    print(f'Lista 3: {lista3} - {len(lista3)}')

if __name__ == "__main__":
    main()