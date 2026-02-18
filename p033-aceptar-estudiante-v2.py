# p033-aceptar-estudiante-v2.py
# Controla el acceso a la universidad en base a dos condiciones

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print(' -- Proceso de Ingreso a la Universidad del Bajio --')

nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))

if edad >= 18:
    print('Ingresa 2 calificaciones separadas por Enter')
    cal1 = float(input())
    cal2 = float(input())
    if cal1 >= 8 and cal2 >= 8:
        print(f'{nombre} BIENVENIDO a la universidad, tu edad y tus calificaciones lo permiten') 
    else:
        print(f'!Lo sentimos {nombre}, se requieren calificaciones mayores a 8')
else:
    print(f'Lo sentimos {nombre} solo permitimos mayores de 18')
    

print('\nProceso Terminado .. gracias por participar')