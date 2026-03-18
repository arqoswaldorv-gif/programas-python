# p101-mes-día-nombre.py
# Leer un número de mes (ej. 4). Guardar los días de cada mes en una lista y los nombres de los meses en otra lista. Asumir 28 días para febrero. Imprimir el nombre del mes y la cantidad de días del mes correspondiente (ej. marzo, 30).

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Mes, día y nombre')

nombres = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = int(input('Introduzca un numero de mes (1-12): '))

if mes >= 1 and mes <= 12:
    print('--- Resultados ---')
    print(f'Mes: {nombres[mes-1]}')
    print(f'Dias: {dias[mes-1]}')