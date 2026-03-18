# p102-listas-aleatorios-suma.py
# Generar 2 listas de 10 números aleatorios cada una. Crear una tercera lista donde el elemento sea la suma de los correspondientes de las listas A y B, solo si AMBOS elementos son impares; de lo contrario, el elemento de la tercera lista será 0. Imprimir las 3 listas.

import random

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Lista de numeros aleatorios')

MAX = 10
lista_a = []
lista_b = []
lista_c = []

for _ in range(MAX):
    lista_a.append( random.randint(1,20) )
    lista_b.append( random.randint(1,20) )

print('\n---Lista Generadas ---')
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')

for i in range(MAX):
    if lista_a[i] % 2 !=0 and lista_b[i] % 2 !=0:
        lista_c.append(lista_a[i] + lista_b[i])
    else:
        lista_c.append(0)

print('\n---Resultaods (Suma solo si A[i] y B[i] son impares) ---')
print(f'Lista C: {lista_c}')