# 047-conteo-descendente-v2.py
# Imprime los numeros de n a 1, con while

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Imprime los numeros de n a 1, con while')

n = int(input('Desde donde? '))
m = int(input('En decrementos de ? '))

r = n

while r >= 1:
    print(r)
    r = r - m
    
print('\nCiclo terminado: {r}')