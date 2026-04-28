# p144-mayor-menor.py
# Funciones para encontrar el mayor y el menos numeros de una lista

from typing import List

def mayor(lista:List[float]) -> float:
    num_mayor = lista[0]
    for numero in lista:
        if numero > num_mayor:
            num_mayor = numero
    return num_mayor

def menor(lista:List[float]) -> float:
    num_menor = lista[0]
    for numero in lista:
        if numero < num_menor:
            num_menor = numero
    return num_menor

def captura_datos() -> List[float]:
    datos : List [float] = []
    print(f"Ingresa un numeor ('fin' para terminar): ")
    while True:
        entrada = input('Numero: ')
        if entrada.lower() == 'fin' : break
        try :
            numero =float(entrada)
            datos.append(numero)
        except ValueError:
            print('Debe ser numero')
    return datos


def main() -> None:
    # numeros : List[float] = [20, 50, 80, 100, 10, 4, 25]

    numeros : List[float] = captura_datos()

    if numeros: 
        num_menor = menor(numeros)
        num_mayor = mayor(numeros)

        print(f'Numeros ingresados : {numeros} - {len(numeros)}')
        print(f'El menor es: {num_menor}')
        print(f'El mayor es: {num_mayor}')
    else:
        print('No se ingresaron numeros')

if __name__ == "__main__":
    main()