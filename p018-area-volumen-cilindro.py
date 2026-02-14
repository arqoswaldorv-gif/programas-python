# p018-area-volumen-cilindro.py
# Crea un programa que calcule el área y volumen de un cilindro. Pide al usuario que ingrese el radio y la altura del
# cilindro. Las fórmulas para el cálculo de área y de volumen son:
# • Area = PI * radio * (radio + alto)
# • Volumen = PI * (Radio * Radio) * Altura

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

import math as mt

print("-" * 40)
print('Calcular área y volumen de un cilindro')
print("-" * 40)


radio = float(input('Ingrese el radio del cilindro: '))
altura = float(input('Ingrese la altura del cilindro: '))

area = mt.pi * radio * (radio + altura)
volumen = mt.pi * (radio * radio) * altura

print("-" * 40)
print(f'El área del cilindro es: {area:.2f}')
print(f'El volumen del cilindro es: {volumen:.2f}')