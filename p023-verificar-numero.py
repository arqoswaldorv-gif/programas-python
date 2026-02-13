# p023-verificar-numero.py
# Verifica si un numero entero es positivo, negativo o cero

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print("Verificando si un numero entero es positivo, negativo o cero \n")

numero = int(input("Dame un numero entero: "))

if numero > 0:
    print("Numero POSITIVO")
if numero < 0:
    print("numero NEGATIVO")
if numero == 0:
    print("Numero CERO")

    print("\n Programa Terminado \n")