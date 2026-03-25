# p105-datos-estudiante.py
# Gestionar datos de un estudiante usando diccionarios

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Gestion de datos de un estudiante')

estudiante = {
    'nombre' : 'Juan Perez',
    'edad' : 45,
    'email' : 'jperez@msn.com',
    'carrera' : 'Sistemas'
}

print(f'\nLos datos del estudiante son : \n\n {estudiante} - {len(estudiante)}')

estudiante['calificacion'] = 9.5
estudiante['email'] = 'jaunp@gmail.com'

print(f'\nLos datos del estudiante son : \n\n {estudiante} - {len(estudiante)}')

print('\nIterar por las llaves')
for k in estudiante.keys():
    print(k)


print('\nIterar por las valores')
for v in estudiante.values():
    print(v)

print('\nIterar por los elementos (items)')
for k, v in estudiante.items():
    print(f'{k:<15} : {v}')