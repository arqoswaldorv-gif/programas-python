# p061-suma-200.py
# Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200. Al terminar, mostrar cuántos números se introdujeron y la suma final.
# Ejemplo de ejecución:
#  Suma actual: 0. Introduce un número: 70
#  uma actual: 70. Introduce un número: 80
#  Suma actual: 150. Introduce un número: 55
#  --------------------
#  Meta de 200 alcanzada.
#  Suma final: 205
#  Total de números introducidos: 3
#  ¿Desea continuar (S/N)? N


while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Números y suma total')
    print('-'*60)
    
    print('Introduce números ( suma >= 200):')
    suma = numero = contador = 0
    while True:
        numero = int(input(f'Suma actual: {suma}. Introduce un número: '))
        suma += numero
        if suma >= 200: break
        contador += 1
        
    
    print('-'*60)
    print('Meta de 200 alcanzada.')
    print(f'Suma final: {suma}')
    print(f'Total de números introducidos: {contador}')
    
    if input('\n¿Deseas continuar (S/N)? ').upper()=='N': break
    
print('\nProceso terminado')