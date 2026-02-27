# p063-numero-mayor.py
# Leer una serie de números hasta que el usuario ingrese un 0. Al terminar, el programa deberá mostrar cuál fue el
# número más grande de todos los introducidos.
# Ejemplo de ejecución:
#   Introduce números (0 para terminar):
#   > 25
#   > 101
#   > 49
#   > 88
#   > 0
#   --------------------
#   El número mayor fue: 101
#   ¿Desea continuar (S/N)? N

while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Números mayor')
    print('-'*60)
    
    print('Introduce números (0 para terminar):')
    mayor  = 0
    while True:
        numero = int(input())
        if numero == 0: break
        if numero > mayor:
            mayor = numero
        
    print('-'*60)
    print(f'El número mayor fue: {mayor}')
    
    if input('\n¿Deseas continuar (S/N)? ').upper()=='N': break
    
print('\nProceso terminado')