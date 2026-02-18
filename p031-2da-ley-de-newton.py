# p031-2da-ley-de-newton.py
# Calcular la fuerza, masa o aceleracion segun la ley de newton

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Calculadora de la segunda ley de Newton')
print('[F ]uerza      - f = m * a')
print('[M ]asa        - m = f / a')
print('[A ]celeracion - a = f / m')
op = input('Opcion ? ').upper()

if op == 'F':
    print('\nCalculando la Fuerza')
    m = float(input('Masa ? '))
    a = float(input('Aceleracion ? '))
    f = m * a
    print(f'La fuerza es: {f:.2f} ')
elif op == 'M':
    print('\nCalculando la Masa')
    f = float(input('Fuerza ? '))
    a = float(input('Aceleracion ? '))
    m = f / a
    print(f'\nLa Masa es: {m:.2f} ')
elif op == 'A':
    print('\nCalculando la Aceleracion')
    f = float(input('Fuerza ? '))
    m = float(input('Masa ? '))
    a = f / m
    print(f'\nLa Aceleracion es: {a:.2f} ')
else:
    print(f'Opcion invalida ...')
    

print('\nProceso temrinado, gracias por utilizar este programa')