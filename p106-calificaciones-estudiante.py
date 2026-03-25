# p106-calificaciones-estudiante.py
# Gestionar calificaciones de un estudiante usando diccionario

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Gestion de datos de un estudiante')

materias = ['Fisica', 'Quimica', 'Matematicas', 'Geografia', 'Estadostoca']
califs = [10, 9, 8, 7.5, 6]

print(f'Lista de materias       :\n{materias}')
print(f'Lista de calificaciones :\n{califs}')

notas = dict(zip(materias,califs))

print(f'Las notas {notas} - {len(notas)}')

notas.update({'Ingles':10, 'Programacion':7})
print(f'Las notas {notas} - {len(notas)}')

notas.pop('Fisica')
notas.popitem()
print(f'Las notas {notas} - {len(notas)}')

notas.update({'Quimica':10, 'Matematicas':10})
print(f'Las notas {notas} - {len(notas)}')

s = 0
print('\nMaterias y calificaciones finales')
for m, c in notas.items():
    print(f'{m:<12} - {c:>5,.2f}')
    s = s + c
    
print(f'La suma es : {s}')
print(f'El promedio es : {s/len(notas)}')

notas.clear()
print(f'Las notas {notas} - {len(notas)}')