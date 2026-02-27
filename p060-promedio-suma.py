# p060-promedio-suma.py
# Leer números introducidos por el usuario hasta que ingrese un 0. Al finalizar, mostrar el conteo total de números, la suma y el promedio de la serie.
# Ejemplo de ejecución:
# Introduce números (0 para terminar):
# > 10
# > 5
# > 15
# > 0
# --------------------
# Se introdujeron 3 números.
# La suma es: 30
# El promedio es: 10.0
# ¿Desea continuar (S/N)? N


while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Números y suma total')
    print('-'*60)
    
    print('Introduce números (0 para terminar):')
    suma = numero = contador = 0
    while True:
        numero = int(input())
        if numero == 0: break
        suma += numero
        contador += 1
        
    promedio = suma // contador
    
    print('-'*60)
    print(f'Se introdujeron {contador} números')
    print(f'La suma es: {suma}')
    print(f'El promedio es: {promedio}')
    
    if input('\n¿Deseas continuar (S/N)? ').upper()=='N': break
    
print('\nProceso terminado')