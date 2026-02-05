# p002-area-circulo.py
# Calcular el area de un circulo

import math # importa el modulo de funciones matematicas

print("calculando el area de un circulo/n/") # / inserta una linea en blanco en la salida

print("Dame el radio? ")
radio = float(input())

area = math.pi *math.pow(radio, 2)

print(f"El circulo de radio {radio:.2f} tiene un area de {area:.2f}")