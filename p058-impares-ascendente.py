# p058-impares-ascendente.py
# Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el usuario.
# Ejemplo de ejecución:
#  Introduce un número límite: 9
#  Números impares: 1, 3, 5, 7, 9
#  La suma de los impares es: 25
#  ¿Desea continuar (S/N)? N

while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Números impares y suma total de 1 a N')
    print('-'*60)
    
    n = int(input('Introduce el número límite: '))
    suma = 0
    i = 1

    while i <= n:
        if i % 2 != 0: 
            print(f'{i}', end=' ')
            suma += i
        i += 1
    
    print('\n')
    print('-'*60)
    print(f'La suma de los imapres es: {suma}')
    
    if input('\n¿Deseas continuar (S/N)? ').upper()=='N': break
    
print('\nProceso terminado')