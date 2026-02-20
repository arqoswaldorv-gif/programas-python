# p046-conteo-descendente.py
# Imprime los numeros de 100 a 1, usando un ciclo while

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Iniciando secuecnia ascendente ...')

c = 100

while c >= 1:
    print(f'{c}', end='')
    c -= 1
    
print('\n Terminado')