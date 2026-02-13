# p023-verificar-numero-v2.py
# Verifica si un numero entero es positivo, negativo o cero

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print("Verificar si un numero es positivo, negativo o cero (versión if else ) \n")

numero = int(input("Dame un numero entero: "))

if numero > 0:
    print("Numero POSITIVO")
else:
    if numero < 0:
        print("El numero es NEGATIVO")
    else:
        print("El numero es CERO")
print("\nAqui ya terminamos de tomar decisiones")