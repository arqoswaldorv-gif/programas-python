# p017-convertir-temperatura.py
# Dada una temperatura en grados celsius, obtener su equivalente en grados farenheit, usando la siguiente formula:
# • farenheit = (celsius × 9/5) + 32

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

print("-" * 40)
print('Convertir temperatura de Celsius a Farenheit')
print("-" * 40)

celsius = float(input('Ingrese la temperatura en grados Celsius: '))

farenheit = (celsius * 9/5) + 32

print("-" * 40)
print(f'La temperatura en grados Farenheit es: {farenheit:.2f}')
print("-" * 40)