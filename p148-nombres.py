# p148-nombres.py
# Funcion que tome dos lista de cadenas y las procese

from typing import List

def une_procesa(l1:List[str], l2:List[str]) -> List[str]:
    todo = l1 + l2
    todo.sort()
    may : List[str] = []
    for nombre in todo:
        may.append(nombre.upper())
    return may

def entrada() -> List[str]:
    datos : List[str] = []
    print('Introduce Nombres (vacio para terminar)')
    while True:
        nombre = input('Nombre: ')
        if nombre == '' : break
        datos.append(nombre)
    return datos

nombres1 : List[str] = ["Ana", "Luis", "Carlos", "Martha", "Sofia"]
nombres2 : List[str] = entrada()
todo : List[str] = une_procesa(nombres1, nombres2)

print(f'Lista nombres 1 : {nombres1} - {len(nombres1)}')
print(f'Lista nombres 2 : {nombres2} - {len(nombres2)}')
print(f'Lista nombres 3 : {todo} - {len(todo)}')