# p064-verificar-palindromo.py
# Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo. Un número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda (ej. 121, 3443).
# Ejemplo de ejecución:
#   Introduce un número para verificar si es palíndromo: 121
#   El número 121 es un palíndromo.
#   ¿Desea continuar (S/N)? S
#   Introduce un número para verificar si es palíndromo: 123
#   El número 123 no es un palíndromo.
#   ¿Desea continuar (S/N)? N


while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Números palíndromo')
    print('-'*60)
    
    numero = input('Introduce números: ')
    indice = 0
    es_palindromo = True
    
    while indice < len(numero):
        
        if numero[indice] != numero[len(numero) - indice - 1]:
            es_palindromo = False
            break
        
        indice += 1
            
    if es_palindromo:
        print(f'El número {numero} es un palíndromo.')
    else:     
        print(f'El número {numero} NO un palíndromo.')
        
    
    if input('\n¿Deseas continuar (S/N)? ').upper()=='N': break
    
print('\nProceso terminado')