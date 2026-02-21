# p036-numeros-consecutivos.py
#  Problema: Escribe un programa que reciba tres números enteros y determine si son consecutivos. Si lo son muestra un mensaje de confirmación; de lo contrario, informa que no lo son.
#Ejemplo de ejecución:
# • Entrada: 9, 10, 11
# • Salida: Los números son consecutivos.
# • Entrada: 1, 4, 6
# • Salida: Los números no son consecutivos.

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('--- Verificar numeros consecutivos ---')

n1 = float(input('Numero 1: '))
n2 = float(input('Numero 2 : '))
n3 = float(input('Numero 3 : '))

if n1 == (n2 -1 ) == (n3 - 2):
    print(f'Los numeros son consecutivos')
else:
    print(f'Los numeros NO son consecutivos')


print('\nProceso terminado ...')