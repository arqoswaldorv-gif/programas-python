# p121-municipios.py
# Gestion de un padron municipal usando conjuntos

municipios = {'Zacatecas', 'Guadalupe', 'Jerez', 'Fresnillo', 'Fresnillo'}

print('\033[H\033[J')
print("--- Gestion de un padron municipal (usando conjuntos) ---")

print(f'Los municipios : {municipios} - {len(municipios)} - {type(municipios)}')

print('\nTodos los municipios uno a uno:')
for municipio in municipios:
    print(municipio, end=' | ')
    
print('\n\n Alta de un municipio al padron : Teul')
municipios.add('Teul')
print(f'Los municipios : {municipios} - {len(municipios)}')

print('\nAgregar varios municipios al padron : Luis Moya, Ojocaliente, Tepetongo')
municipios.update({'Luis Moya', 'Ojocaliente', 'Tepetongo'})
print(f'Los municipios : {municipios} - {len(municipios)}')

print('\nBaja de un municipio con remove() : Zacatecas')
municipios.remove('Zacatecas')
print(f'Los municipios : {municipios} - {len(municipios)}')

print('\nBaja de un municipio con discard() : Ojocaliente')
municipios.discard('Ojocaliente')
print(f'Los municipios : {municipios} - {len(municipios)}')

print('\nBaja del padron con pop() : x? ')
eliminado = municipios.pop()
print(f'Los municipios : {municipios} - {len(municipios)} - {eliminado}')

print('\nLimpiar el padron con clear() ')
municipios.clear()
print(f'Los municipios : {municipios} - {len(municipios)}')