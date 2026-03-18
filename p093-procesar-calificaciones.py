# p093-procesar-calificaciones.py
# Procesar las calificaciones de un alumno, usando una lsita

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Pricesar las calificaciones de un alumno')

calificaciones = []

while True:
    try:
        cal = float(input('Calificacion > '))
        if cal == 99: break
        if 0 <= cal <= 10:
            calificaciones.append(cal)
        else:
            print('Calificacion no valida')
    except:
        print('Error: Entrada no valida')

if not calificaciones:
    print('No se capturaron calificaciones')
else: 
    suma = sum(calificaciones)
    promedio = suma/ len(calificaciones)
    mayores_promedio = []
    for cal in calificaciones:
        if cal > promedio:
            mayores_promedio.append(cal)
            
print(f'Se Capturaron {len(calificaciones)} calificaciones')
print(f'Las calificaciones fueron {calificaciones}')
print('\nEstadisticas del Curso')
print(f'Suma     : {sum(calificaciones)}')
print(f'Promedio : {sum(calificaciones) / len(calificaciones)}')
print(f'Calificaicones mayores al promedio {len(mayores_promedio)} y son {mayores_promedio}')
print(f'Calificaicon mas alta : { max(calificaciones) }')
print(f'Calificaicon mas baja : { min(calificaciones) }')