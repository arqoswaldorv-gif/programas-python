# p021-distancia-entre-puntos.py
# Crea un programa que calcule la distancia entre dos puntos en un plano cartesiano. El programa debe pedir al usuario
# que ingrese las coordenadas (x,y) del punto A y las coordenadas (x,y) del punto B. Utiliza la siguiente fórmula para
# calcular la distancia:
# d = √((ax - bx)² + (ay - by)²)

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

import math as mt

print("-" * 40)
print('Calcular distancia entre dos puntos')
print("-" * 40)

ax = float(input('Ingrese la coordenada x del punto A: '))
ay = float(input('Ingrese la coordenada y del punto A: '))
bx = float(input('Ingrese la coordenada x del punto B: '))
by = float(input('Ingrese la coordenada y del punto B: '))

distancia = mt.sqrt((ax - bx) ** 2 + (ay - by) ** 2)

print("-" * 40)
print(f'La distancia entre los puntos A y B es: {distancia:.2f}')