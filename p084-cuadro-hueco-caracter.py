# p084-cuadro-hueco-caracter.py
# El programa debe solicitar al usuario que ingrese el tamaño del lado de un cuadrado y el carácter con el que se dibujará. Luego, deberá imprimir en la consola un "cuadrado hueco", donde el carácter solo se utilice para dibujar el contorno del mismo.

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla


tamaño = int(input('Tamaño del lado del cuadrado: '))
caracter = input('Caracter: ')

for i in range(tamaño):
    for j in range(tamaño):
        if i == 0 or i == tamaño -1:
            print(caracter, end=' ')
        elif j == 0 or j == tamaño -1:
            print(caracter, end=' ')
        else:
            print(' ', end=' ')
        
    print()