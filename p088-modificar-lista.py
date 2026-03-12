# p088-modificar-lista.py
# Muesta como modificar lso elemetnos de una lsita

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Modificar a los elemetnos de una lsita')

califs = [10,9,8,5,6.5,9.8,7,7,6.2,9.5]

print(f'Todas las calificaciones: {califs} - {len(califs)}')

print('\nModificar [0] y [1] con 7 y 7:')
califs[0] = 7
califs[1] = 7
print(f'Resutlado: {califs}')

print('\nModificar el rnago [2:5] (5 no se incluye) con 9,9,9:')
califs[2:5] = [9,9,9]
print(f'Resultado: {califs} - {len(califs)}')