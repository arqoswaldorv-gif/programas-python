# p079-factorial-numeros.py
# Calcular el factorial de n numeros

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print("--- Calcular el factorial de n numeros ---")

try :
    n = int(input("Cuantos factorailes ? "))

    for i in range(1, n+1):

        factorial = 1
        for j in range(1, n+ 1):
            factorial *= j

    print(f'Factorial de {n}! es = {factorial}')
except ValueError:
    print('Error: se esperaba un numero entero')