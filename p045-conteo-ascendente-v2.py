# p045-conteo-ascendente-v2.py
# Imprime los numeros de  1 a 100 un ciclo while

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Iniciando secuecnia ascendente ...')

n = int(input('Hasta donde ? '))
m = int(input('De cuanto en cuanto ?'))

c = 1

while c <= n:
    print(f' {c}', end='')
    c += m

print('\n Secuencia Completada')