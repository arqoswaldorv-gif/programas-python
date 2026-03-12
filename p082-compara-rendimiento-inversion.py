# p082-compara-rendimiento-inversion.py
# Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años. El usuario debe ingresar el monto inicial y la tasa de interés anual (porcentaje) para cada uno de los dos fondos, así como el número de años a proyectar. El programa deberá mostrar una tabla comparativa anual y al final indicar qué fondo generó un mayor rendimiento.

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

monto_a = int(input('Monto inicial del fondo A: '))
tasa_interes_anual_a = float(input('Tasa de interes anual (%): '))

monto_b = int(input('Monto inicial del fondo B: '))
tasa_interes_anual_b = float(input('Tasa de interes anual (%): '))

numero_anios = int(input('Numero de años a proyectar: '))

print('--- Fondo de INversion A ---')
print(f'Monto inical: {monto_a}')
print(f'Tasa de Interes anual (%): {tasa_interes_anual_a}')

print('--- Fondo de Inversion B ---')
print(f'Monto inical: {monto_b}')
print(f'Tasa de Interes anual (%): {tasa_interes_anual_b}')

print('--- Comparacion de Rendimetio Anuales ---')
print('Año  |  Fonfo A  |  Fonfo B')
print('----------------------------------------')
for i in range(numero_anios):
    monto_a = monto_a * (1 + tasa_interes_anual_a / 100)
    monto_b = monto_b * (1 + tasa_interes_anual_b / 100)
    print(f'{i+1:2d}    |  {monto_a:10.2f}  |  {monto_b:10.2f}')

if monto_a > monto_b:
    print(f'El fondo A {monto_a:.2f} supero al Fondo B {monto_b:.2f}')
else:
    print(f'El fondo B {monto_b:.2f} supero al Fondo A {monto_a:.2f}')