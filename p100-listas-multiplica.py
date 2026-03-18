# p100-listas-multiplica.py
# Leer dos listas, cada una con 5 elementos numéricos. Crear una tercera lista multiplicando los elementos de las dos listas correspondientes. Imprimir las tres listas.
# Ejemplo:
# Introduzca 5 números para la Lista A: 2 4 6 8 10
# Introduzca 5 números para la Lista B: 5 1 3 7 9

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Multiplciar dos listas')

lista_a = []
lista_b = []
lista_c = []

print('Introduzca 5 números para la Lista A:')
for _ in range(5):
    a = int(input())
    lista_a.append(a)

print('Introduzca 5 números para la Lista B:')
for _ in range(5):
    b = int(input())
    lista_b.append(b)

for i in range(5):
    c = lista_a[i] * lista_b[i]
    lista_c.append(c)

print('--- Resultados ---')
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')
print(f'Lista C (A * B): {lista_c}')