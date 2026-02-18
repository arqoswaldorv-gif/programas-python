# p032-aceptar-estudiante.py
# Controla el acceso a la universidad en base a dos condiciones

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print(' -- Proceso de Ingreso a la Universidad del Bajio --')

nombre = input('Dame tu nombre ? ')
edad = int(input('Edad ? '))

if edad < 18:
    print(f'Lo sentimos, {nombre}. Solo aceptamos mayores de 18')
else:
    print('Ingresa 2 calificaciones separadas por Enter')
    cal1 = float(input())
    cal2 = float(input())
    if cal1 < 8 or cal2 < 8:
        print(f'Lo sentimos {nombre} se requiren calificaciones mayores a 8')
    else:
        print(f'{nombre} BIENVENIDO a la universidad, tu edad y tus calificaciones lo permiten')
        
    
print('\nProceso Terminado .. gracias por participar')