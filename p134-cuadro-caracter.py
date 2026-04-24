# p137-temperatura.py
print('\033[H\033[J')

def dibuja_cuadro(ren:int, col:int, car:str) -> None:
    for r in range(ren):
        for c in range(col):
            print(car, end='')
        print('')
    print('')

# dibuja_cuadro(4,10,'*')
# dibuja_cuadro(3,5,'#')

ren = int(input('Renglones ? '))
col = int(input('Columnas ? '))
car = input('Caracter ? ')

dibuja_cuadro(ren, col, car)