# p103-ciudades.py
# Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $. Imprimir:
# • Cuántos elementos tiene la lista.
# • La lista completa.
# • La lista ordenada en orden descendente.
# • Cuántas ciudades inician con una letra consonante y sus nombres.

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Lista de Ciudades')

ciudades = []
lista_descendente = [] 
lista_consonantes = []

while True:
    ciudad = input('Introduzca nombre de ciudad ($ para detener): ')
    if ciudad == '$': break
    ciudades.append(ciudad)

lista_descendente = sorted(ciudades, reverse=True)

for ciudad in ciudades:
    if ciudad[0] not in "aeiouAEIOU":
        lista_consonantes.append(ciudad)


print('--- Resultados ---')
print(f'Total de ciudades introducidas: {len(ciudades)}')
print(f'Lista original: {ciudades}')
print(f'\nLista ordenada descendente: {lista_descendente}')
print(f'\nCiudades que inician con consonante: {len(lista_consonantes)}')
print(f'Lista de ciudades con consonante inicial: {lista_consonantes}')