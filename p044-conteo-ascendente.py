# p044-conteo-ascendente.py
# Imprime los numeros de  1 a 100 un ciclo while

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Iniciando secuencia ascendente ...')

c = 1

while c <= 20:
    print(f' {c}', end='')
    c += 1

print('\n Secuencia Completada')