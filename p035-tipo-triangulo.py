# p035-tipo-triangulo.py
# Clasificar un triagnulo segun la longitud de sus lados

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('-- Clasificador de traingulos --')

l1 = float(input('Lado 1 ? '))
l2 = float(input('Lado 2 ? '))
l3 = float(input('Lado 3 ? '))

if l1 == l2 == l3:
    print('EQUILATERO')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('ISOCELES')
else:
    print('ESCALENO')


print('\nAdios, gracias por utilizar este programa')