# p055-tabla-multiplicar-while-v2.py
# Imprime la tabla de 1 a n, desde 1 hasta m

while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Tablas de Multiplicar')
    
    while True:
        n = int(input('Hata que tabla quieres ?'))
        m = int(input('Hasta donde la queires ?'))
        if n>0 and m>0 : break
        print('Error, los valores son incorrectos')
        
    t = 1
    while t <= n:
        print(f'\nTabla {t}')
        c = 1
        while c <= m:
            print(f'{t} x {c} = {t*c}')
            c += 1
        
        t += 1
    
    
    if input('\nDesases Conitnuar (S/N)? ').upper()=='N': break
    
print('\nProceso terminado')