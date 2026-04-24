# p139-factorial.py

def factorial(num:int) -> int:
    if num < 0:
        return -1
    res = 1
    for i in range(2, num+1):
        res = res * i
    return res

# print(f'Factorial de 5 es {factorial(5)}')
# print(f'Factorial de 1 es {factorial(-1)}')

def main() -> None:
    print('\033[H\033[J')
    num = int(input('Numero: '))
    res = factorial(num)
    if res == -1:
        print('Error al calcular el factorial')
    else:
        print(f'El factorail de {num} es {res}')


if __name__ == "__main__":
    main()