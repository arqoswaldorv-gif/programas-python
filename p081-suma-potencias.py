# p081-suma-potencias.py
# SUma de potencias de un numero x desde x^1 hasta x^n

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

x = int(input('Valor de X : '))
n = int(input('Valor de n : '))

suma_total = 0

termino_actual = 1
for j in range(n+1):
    suma_total += termino_actual
    print(f'Termino {x}^{j} = {termino_actual}')
    termino_actual *= x
    
    
print('\nSuma de toda la serie :' , suma_total)