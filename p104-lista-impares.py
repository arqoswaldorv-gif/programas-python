# p104-lista-impares.py
# Leer un entero n. Llenar una lista con los primeros n números impares.
# Calcular e imprimir:
# • La suma y el promedio de los números.
# • Los números que son divisibles entre 3 y su suma.
# • Pedir un elemento a buscar en la lista original e indicar si está y en qué posición (índice).

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Lista de numeros impares')

lista_impares = []
lista_divisible_3 = []

n = int(input('Introduzca la cantidad de numeros imapres (n) : '))
numero = 0
for i in range(n):
    numero = 2 * i + 1
    lista_impares.append(numero)
    if numero % 3 == 0:
        lista_divisible_3.append(numero)

print('--- Generación de Lista ---')
print(f'Lista de los primeros {n} números impares: {lista_impares}')

print('\n--- Calculos ---')
print(f'Suma de los numeros : {sum(lista_impares)}')
print(f'Promedio de los numeros: {sum(lista_impares) / len(lista_impares)}')

print('\n--- Divisibles entre 3 ---')
print(f'Numeros divisibles entre 3: {lista_divisible_3}')
print(f'Suma de los numeros divisibles entre 3: {sum(lista_divisible_3)}')

print('\n--- Busqueda ---')
elemento = int(input('Introduzca el numero a buscar: '))
if elemento in lista_impares:
    print(f'Result: EL elemento {elemento} esta en la lista en la posicion (índice) {lista_impares.index(elemento)}')
else: 
    print(f'Result: El elemento {elemento} no esta en la lista')