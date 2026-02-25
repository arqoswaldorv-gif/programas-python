# p054-tabla-multiplicar-while-v1.py
# Imprime la tabla de multiplicar t hasta n

while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Imprime la talba de multilplicar t hasta n')
    
    while True:
        t = int(input('Tabla      :'))
        n = int(input('Hata donde :'))
        if t>0 and n>0 : break
        print('Error, los valores son incorrectos')
        
    c = 1
    while c <= n:
        print(f'{t} x {n} = {t*c}')
        c += 1
    
    
    if input('\nDesases Conitnuar (S/N)? ').upper()=='N': break
    
print('\nProceso terminado')