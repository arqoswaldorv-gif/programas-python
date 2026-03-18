# p097-procesar-datos-sensores.py
# SImular la recoleccion de datos de dos sensores y procesar als lecturas

import random

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Simulando la recoleccion de datos de dos sensores')

MAX = 10
sensor_a = []
sensor_b = []
todo = []

for _ in range(MAX):
    sensor_a.append( random.randint(1,10) )
    sensor_b.append( random.randint(1,10) )

print('\n---Reporte de Lecturas de sensores ---')
print(f'Sensor A: {sensor_a}')
print(f'Sensor B: {sensor_b}')

for i in range(MAX):
    sensor_a[i] = sensor_a[i] ** 2
    sensor_b[i] = sensor_b[i] ** 2
    todo.append(sensor_a[i] + sensor_b[i])


print('\n---Reporte de Lecturas de sensores ---')
print(f'Sensor A: {sensor_a}')
print(f'Sensor B: {sensor_b}')