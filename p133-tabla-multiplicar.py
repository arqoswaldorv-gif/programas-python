# p133-tabla-multiplicar.py
# Imprime la tabla de multiplicar desseada, ahsta el limite desaeado, usadno uan funcion
print('\033[H\033[J')

def tabla_multiplicar(tabla:int, limite:int) -> None:
    print(f'Tabla de multiplicar del {tabla} hasta el {limite} ')
    for i in range(1, limite + 1):
        res = tabla * 1
        print(f'{tabla} x {i} = {res}')
    print()

# tabla(5,10)
# tabla(3,20)

tabla = int(input('Ingresa la tabla de multiplucar que deseas (ej. 5): '))
limite = int(input('Ingresa el limite de multiplucar que deseas (ej. 10): '))

tabla_multiplicar(tabla, limite)