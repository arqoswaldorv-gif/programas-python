# p138-suma-digitos.py

def suma_digitos(num:int) -> int:
    s = 0
    for n in str(num):
        s = s + int(n)
        print(n)
    return s

# print(f'SUma 1971 : {suma_digitos(1971)}')

def main() -> None:
    print('\033[H\033[J')
    n = int(input('Numero: '))
    res = suma_digitos(n)
    print(f'La suma es {res}')


if __name__ == "__main__":
    main()