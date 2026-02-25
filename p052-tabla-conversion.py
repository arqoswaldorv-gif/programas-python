# p052-tabla-conversion.py
# Mostrar una tabla de conversion de Peso a Dolares

tc = 20.71

while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Tabla de Conversion de Peso a Dolares')
    print(f'Tipo de cambio : {tc} peso x Dolar')
    print('-'*15)
    
    while True:
        pi = float(input('Valor inicial : '))
        pf = float(input('Valor final   :'))
        if (pi>0 and pf>0) and (pi<pf): break
        print('Error en los valores de entrada, intenta de nuevo')
    
    c = pi
    print('\nPesos\t\tDolar')
    print('-'*25)
    while c <= pf:
        print(f'{c:.2f}\t\t{c/tc:.2f}')
        c+=1
    print('-'*25)
    
    if input('Desases Conitnuar (S/N)? ').upper()=='N': break
    

print('\nProceso Terminado')