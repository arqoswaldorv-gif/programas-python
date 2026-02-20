# p051-adivina-numero.py
# Permite al usuario adivinar un numero generado al azar

import random

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Permite al usuario adivinar un numero generado al azar entre 1 y 50')

n = random.randint(1,50)

ci = 0

while True:
    i = int(input('Tu numero ? '))
    ci += 1
    
    if i < n :
        print('Demasiado BAJO, Intenta con un número más alto')
    elif i > n:
        print('Demasiado ALTO, Intenta con un número más bajo')
    else: 
        print(f'\nFelicidades, Adivinaste el numero secreto : {n}')
        print(f'Lo lograste en {ci} intentos !')
        break
print("\nTermina el juego")