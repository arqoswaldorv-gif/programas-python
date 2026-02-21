# p038-dia-semana.py
#  Problema: Escribe un programa que solicite un número entero del 1 al 7 y muestre el día de la semana correspondiente, considerando que 1 es domingo y 7 es sábado. Si el número ingresado está fuera de ese rango, debe mostrar un mensaje de error.
# Ejemplo de ejecución:
# • Entrada: 2
# • Salida: Lunes
# • Entrada: 8
# • Salida: Error: Día inválido.

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('--- Verificar dia de la semana ---')

numero = float(input('Ingrese un numero: '))

if numero == 1:
    print(f'Domingo')
elif numero == 2:
    print(f'Lunes')
elif numero == 3:
    print(f'Martes')
elif numero == 4:
    print(f'Miercoles')
elif numero == 5:
    print(f'Jueves')
elif numero == 6:
    print(f'Viernes')
elif numero == 7:
    print(f'Sabado')
else:
    print(f'Error: Dia invalido')
    
print('\nProceso terminado ...')