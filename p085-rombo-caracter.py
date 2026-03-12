# p085-rombo-caracter.py
# Solicitar al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo. El programa deberá dibujar el rombo utilizando el carácter que el usuario elija.

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

impar = int(input('Numero impar (Altura y Ancho maximo): '))
caracter = input('Caracter: ')

for i in range(impar):
    if i > impar // 2:
        espacios = i - impar // 2
    else:
        espacios = (impar // 2 )- i
    for k in range(espacios):
        print(' ', end='')
        
    
    if i > impar // 2:
        caracteres = 2 * (impar - i) - 1
    else:
        caracteres = 2 * i + 1

    for j in range(caracteres):
        print(f"{caracter}", end='')
        
        
    print()