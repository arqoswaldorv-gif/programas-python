# p086-triangulo-invertido-numeros.py
# Solicitar al usuario un número entero n que determinará la altura de un triángulo numérico invertido. El programa debe imprimir n renglones. El primer renglón contendrá los números de 1 a n, el segundo de 1 a n-1, y así sucesivamente hasta que el último renglón contenga solo el número 1.

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

n = int(input('Numero: '))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()