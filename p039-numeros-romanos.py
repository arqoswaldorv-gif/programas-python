# p039-numeros-romanos.py
# Problema: Escribe un programa que pida al usuario un número entero entre 1 y 10 y muestre su equivalente en números romanos. Si el número está fuera de este rango, debe mostrar un mensaje de error.
# Ejemplo de ejecución:
# • Entrada: 4
# • Salida: IV
# • Entrada: 11
# • Salida: Error: Número inválido.

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('--- Verificar numeros romanos ---')

numero = float(input('Ingresa un numero entre 1 y 10:'))

if numero == 1:
    print('I')
elif numero == 2:
    print('II')
elif numero == 3:
    print('III')
elif numero == 4:
    print('IV')
elif numero == 5:
    print('V')
elif numero == 6:
    print('VI')
elif numero == 7:
    print('VII')
elif numero == 8:
    print('VIII')
elif numero == 9:
    print('IX')
elif numero == 10:
    print('X')
else:
    print('Error: Numero invalido')

print('\nProceso terminado ...')