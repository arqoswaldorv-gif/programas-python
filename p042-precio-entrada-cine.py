# p042-precio-entrada-cine.py
# Problema: Crea un programa para la taquilla de un cine que determine el precio de una entrada según la edad del cliente. El programa debe solicitar la edad y mostrar el precio correspondiente, siguiendo estas reglas:
# • Menores de 5 años: Entran gratis.
# • Niños (5 a 12 años): Pagan $5.
# • Adultos (13 a 64 años): Pagan $10.
# • Tercera edad (65 años o más): Pagan $7.
# Ejemplos de ejecución:
# • Entrada: Edad: 4
# • Salida: Tu entrada es gratis.
# • Entrada: Edad: 10
# • Salida: El precio de tu entrada es de $5.
# • Entrada: Edad: 35
# • Salida: El precio de tu entrada es de $10.

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('--- Verificar precio de entrada ---')

edad = int(input('Dame tu edad: '))

if edad < 5: 
    print('Tu entrada es gratis.')
elif edad < 13:
    print('El precio de tu entrada es de $5')
elif edad < 65:
    print('El precio de tu entrada es de $10')
elif edad < 100:
    print('El precio de tu entrada es de $7')
else:
    print('Ya te moriste')

print('\nProceso terminado ...')