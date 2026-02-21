# p037-numero-mayor.py
# Problema: Escribe un programa que reciba tres números enteros e identifique y muestre cuál de ellos es el mayor.
#Ejemplo de ejecución:
# • Entrada: 11, 30, -1
#• Salida: El número mayor es 30.

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('--- Verificar numero mayor ---')

n1 = float(input('Numero 1: '))
n2 = float(input('Numero 2 : '))
n3 = float(input('Numero 3 : '))

if n1 > n2 and n1 > n3:
    print(f'El numero mayor es {n1}')
elif n2 > n1 and n2 > n3:
    print(f'El numero mayor es {n2}')
else:
    print(f'El numero mayor es {n3}')
    
print('\nProceso terminado ...')