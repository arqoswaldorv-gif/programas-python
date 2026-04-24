# p132-funcion-retorno.py
# FUncion que regresa valores

print('\033[H\033[J')

def suma(n1:float, n2:float) -> float:
    return n1 + n2


print('Suma de dos numeros constantes')
suma_res = suma (10,20)
print(f'La sumaa es: {suma_res}')

print("\nDame dos Valores separados pro enter")
a , b = int(input()), int(input())
print(f"La suma es : {suma(a,b )}")