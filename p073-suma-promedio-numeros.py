# p073-suma-promedio-numeros.py
# SUma y promedio n numeros introducidos por el usuario

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

while True:

    
    print('Suma y pormediando numeros')
    
    n = int(input('Cuatnas calificaciones ? '))
    suma = 0
    numeros = ""
    
    for i in range(1, n+1):
        cal =int(input(f'Calificacion {i} : '))
        suma += cal
        numeros += str(cal) + ' '
    
    
    print(f'Las calificaciones fueron : {numeros}')
    print(f'La suma es : {suma}')
    print(f'El Promedio es : {suma/n}')
    
    
    if input('\n\nDesea continuar (S/N) ? ').upper()=='N' : break

print("\nProceso Terminado")