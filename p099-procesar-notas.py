# p099-procesar-notas.py
# Leer un número indeterminado de notas (calificaciones) entre 0 y 100, deteniéndose cuando el usuario introduzca un 0. Validar que todas las notas introducidas estén dentro del rango [0,100]. 
# Calcular e imprimir:
# • Cuántas notas se introdujeron.
# • La lista de notas completa.
# • La suma y el promedio de las notas.
# • La nota máxima y la nota mínima.
# • Cuántas notas y cuáles son las notas menores al promedio.

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Procesar notas de estudiantes')

notas = []
menores_promedio = []

while True:
    nota = int(input('Introduczac Nota (0 para detener) : '))
    if nota == 0 : break
    try: 
        if nota < 0 or nota > 100:
            print('! ERROR ! - Entrada inválida, debde ser 0-100')
        else: 
            notas.append(nota)
        
    except ValueError:
        print('Valor erroneo')

for nota in notas:
    if nota < sum(notas) /len(notas):
        menores_promedio.append(nota)

print(f'Total de notas introducidas: {len(notas)}')
print(f'Lista de notas: {notas}')
print(f'Suma de notas: {sum(notas)}')
print(f'Promedio de notas: {sum(notas) / len(notas)}')
print(f'Nota máxima: {max(notas)}')
print(f'Nota mínima: {min(notas)}')
print(f'Total de notas menores al promedio : {len(menores_promedio)}')
print(f'Lista de notas menores al promedio: {menores_promedio}')