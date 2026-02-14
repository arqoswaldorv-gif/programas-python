# p016-tercer-angulo.py
# Calcular el tercer angulo de un triangulo
# Dados dos ángulos de un triángulo, calcular el 3er ángulo, usando la siguiente formula:
#  • angulo3 = 180 – (angulo1 + angulo2)

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

print("-" * 40)
print('Tercer angulo de un triangulo')
print("-" * 40)

angulo1 = float(input('Ingrese el valor del angulo 1: '))
angulo2 = float(input('Ingrese el valor del angulo 2: '))

angulo3 = 180 - (angulo1 + angulo2)

print(f'Los angulos ingresados son: {angulo1} y {angulo2}')
print(f'El tercer angulo del triangulo es: {angulo3:.2f}')