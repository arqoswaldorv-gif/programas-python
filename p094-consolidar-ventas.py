# p094-consolidar-ventas.py
# Consolidar las ventas de dos sucursales, las ventas las captura el usuario

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Consolidar ventas de las dos sucursales')

ventas = int(input('Cuantas ventas por sucursal ? '))

ventas1 = []
ventas2 = []
todo = []

print('\nDame las ventas de la priemra sucursal')
for i in range(ventas):
    venta = int(input(f'Venta de dia {i+1} ? '))
    ventas1.append(venta)

print('\nDame las ventas de la segunda sucursal')
for i in range(ventas):
    venta = int(input(f'Venta de dia {i+1} ? '))
    ventas2.append(venta)
    
print('\nConsolidando las ventas')
for i in range(ventas):
    sumadia = ventas1[i] + ventas2[i]
    todo.append(sumadia)
print('\nReporte de ventas')
print(f'Sucursal 1  : {ventas1}')
print(f'Sucursal 2  : {ventas2}')
print(f'Consolidado : {todo}')