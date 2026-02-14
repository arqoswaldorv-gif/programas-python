# p015-hipotenusa-triangulo.py
# Calcular la hipotenusa de un triángulo rectángulo
# Se desea calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados, usando la siguiente formula:
#  • hipotenusa = raizcuadrada( longlado1 * lognlado1 + longlado2 * longlado2 )

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

import math as mt

print("-" * 40)
print('Hipotenusa de triangulo')
print("-" * 40)

lado1 = float(input('Ingrese el valor del lado 1: '))
lado2 = float(input('Ingrese el valor del lado 2: '))
lado3 = float(input('Ingrese el valor del lado 3: '))

hipotenusa = mt.sqrt(lado1 * lado1 + lado2 * lado2)

print("Valores ingresados:")
print(f'Lado 1: {lado1},  Lado 2: {lado2},  Lado 3: {lado3}')
print(f'La hipotenusa del triangulo es: {hipotenusa:.2f}')