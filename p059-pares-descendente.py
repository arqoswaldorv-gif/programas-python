# p059-pares-descendente.py

# Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el usuario.
# Ejemplo de ejecución:
# Introduce un número límite (menor a 100): 92
# Números pares: 100, 98, 96, 94, 92
# La suma de los pares es: 480
# ¿Desea continuar (S/N)? N



while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Números pares y suma total, descendente desde 100 hasta n ')
    print('-'*60)
    
    n = int(input('Introduce el número límite (menor a 100): '))
    suma = 0
    i = 100

    while i >= n:
        if i % 2 == 0: 
            print(f'{i}', end=' ')
            suma += i
        i -= 1
    
    print('\n')
    print('-'*60)
    print(f'La suma de los pares es: {suma}')
    
    if input('\n¿Deseas continuar (S/N)? ').upper()=='N': break
    
print('\nProceso terminado')