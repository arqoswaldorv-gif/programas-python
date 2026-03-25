# p107-nombres-edades.py
# Gesion de nombres y edades simuladno un censo, con diccionarios

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Gestion de nombres y edades simuladno un censo, con diccionarios')

datos = {}

print('Introduce nombre sy edades (nombre vacio para termianr) : ')

while True:
    nombre = input('Dame el nombre : ')
    if nombre == '': break
    datos[nombre] = int(input('Edad: '))
    
print(f'\nCenso de nombre y edades : {datos} - {len(datos)}')

s = 0
for n,e in datos.items():
    print(f'{n:<20} - {e:>2}')
    s = s + e

print(f'La suma es : {s}, el promedio es {s/len(datos):.2f}')