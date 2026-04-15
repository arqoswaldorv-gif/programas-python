# p111-lote-autos.py
# Crear una lista de diccionarios

autos = [
    {'marca': 'Ford', 'Modelo': 'Mustang', 'año': 1964},
    {'marca': 'VW', 'Modelo': 'Jetta', 'año': 2015}
]

print('\033[H\033[J')
print('Lista de autos}n')

print(f'\nAutos:  {autos} - {len(autos)}')

autos.append({'marca': 'Chevrolet', 'Modelo': 'Captiva', 'anio': 2024})

print(f'\nAutos:  {autos} - {len(autos)}')

print('\nCada auto dentro de los autos')
for auto in autos:
    print(auto)

print(f'Datos de los autos en forma de tabla')
print('-'*50)
for k in autos[0].keys():
    print(f'{k}\t', end='')
print()
print('-'*50)


for auto in autos:
    for v in auto.values():
        print(f'{v}\t\t', end='')
    print()
print('-'*50)


print(f'\nDatos en forma de registro')
print('-'*50)
suma_años = 0
for auto in autos:
    suma_años = suma_años + auto['año']
    for k, v in auto.items():
        print(f'{k:<12} : {v:>12}')
    print()
print('-'*50)

print('Suma  años : ', suma_años)