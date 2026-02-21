# p043-calculadora-año-bisiesto.py 
# Problema: Escribe un programa que determine si un año, ingresado por el usuario, es bisiesto. Un año es bisiesto si cumple una de las siguientes condiciones:
# 1. Es divisible por 4, pero no es divisible por 100.
# 2. Es divisible por 400.
# El programa debe indicar claramente si el año es bisiesto o no.
# Ejemplos de ejecución:
# • Entrada: 2024
# • Salida: El año 2024 es bisiesto. (Porque es divisible por 4 pero no por 100).
# • Entrada: 1900
# • Salida: El año 1900 no es bisiesto. (Porque es divisible por 100 pero no por 400).
# • Entrada: 2000
# • Salida: El año 2000 es bisiesto. (Porque es divisible por 400).
# • Entrada: 2023
# • Salida: El año 2023 no es bisiesto. (Porque no es divisible por 4).

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('--- Verificar año bisiesto ---')

año = int(input('Dame un año: '))

if año % 400 == 0:
    print(f'El año {año} es bisiesto. (Porque es divisible por 400).')
elif año % 100 == 0:
    print(f'El año {año} no es bisiesto. (Porque es divisible por 100 pero no por 400).')
elif año % 4 == 0:
    print(f'El año {año} es bisiesto. (Porque es divisible por 4 pero no por 100).')
else:
    print(f'El año {año} no es bisiesto. (Porque no es divisible por 4).')
    
print('\nProceso terminado ...')