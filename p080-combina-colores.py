# p080-combina-colores.py
# Genera las combinaciones posibles entre colores

# colores = ['rojo','verde', 'azul', 'cafe']

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('--- Combinaciones Posibles de varios colores ---')
colores = input('Colores separados por coma ').strip().split(',')

for i in colores:
    for j in colores:
        if i != j:
            print(f'{i} - {j}')