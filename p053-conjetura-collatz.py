# p053-conjetura-collatz.py
# Calcular la conjetura de Collatz

while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Imprime la conjetura de Collat')
    pasos = 0
    while True:
        num = int(input('Dame un numero entero positivo > '))
        if num>0: break
        print('Error, el numero debe ser positivo')

    while True:
        if num==1: break
        print(num, end=' ')
        if num%2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        pasos = pasos + 1
    
    print(num, end ='')
    print('\nPasos : ' + str(pasos+1))
    
    
    if input('\nDesases Conitnuar (S/N)? ').upper()=='N': break
    

print('\nProceso terminado')