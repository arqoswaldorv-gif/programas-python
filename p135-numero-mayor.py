# p138-suma-digitos.py
print('\033[H\033[J')

def numero_mayor(n1:int, n2:int, n3:int) -> int:
    may = n1
    if n2 > may:
        may = n2
    if n3 > may:
        may = n3
    return may

print('Dame tres nuemros separado por enter')
a, b, c = int(input()), int(input()), int(input())
print(f'El mayor de 10,20,30: {numero_mayor(a,b,c)}')