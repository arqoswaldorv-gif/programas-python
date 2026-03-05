# p072-suma-pares-impares.py
# Imprimir numeros pares e impares, y su suma, el usuario elige

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

while True:
   
    
    print('Imprimir numeros pares o impares ascendente y su suma')
    print('[ 1 ] Pares')
    print('[ 2 ] Impares')
    op = int(input('Elige : '))
    
    s = 0
    
    if op == 1:
        print(f'\nImprime numeros Pares y su suma')
        n = int(input('\nLimite: '))
        for i in range(2, n+1, 2):
            print(i, end=' ')
            s += i
        print('\nSuma de pares: ' + str(s))
    elif op == 2:
        print(f'\nImprime numeros Impares y su suma')
        n = int(input('\nLimite: '))
        for i in range(1, n+1, 2):
            print(i, end=' ')
            s += i
        print('\nSuma de Impares: ' + str(s))
    else:
        print('\n\nOpcion Invalida')
    
    if input('\n\nDesea continuar (S/N) ? ').upper()=='N' : break

print("\nProceso Terminado")