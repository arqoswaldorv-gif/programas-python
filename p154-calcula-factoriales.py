# p154-calcula-factoriales.py
# Desarrolla un porgram que calcule el factorial de cada numero de una lsita. Debes implemtar
# 1.- Una funcion que lea y devuelva una lista de nuemro enteros
# 2.- Una funcion que reciba un numero entero y devuelva su factorial (ej: 5 -> 120)
# 3.- Una funcion principal que reciba la lista de numeros. Esta debe usar la funcion factorial para crear y devolver una nueva lista con los factoriales de cada factorial de cada numero
# El progrma debe imprimir la lista original y la lista de facotrial

from typing import List

def leer_numeros() -> List[int]:
    entrada = input("Dame los números (separados por espacio): ")
    numeros_str = entrada.split()
    numeros: List[int] = []
    for num_str in numeros_str:
        numeros.append(int(num_str))
    return numeros

def factorial(num: int) -> int:
    if num < 0:
        return 1
    res = 1
    for i in range(2, num + 1):
        res = res * i
    return res

def procesar_lista(lista: List[int]) -> List[int]:
    resultado: List[int] = []
    for numero in lista:
        fact = factorial(numero)
        resultado.append(fact)
    return resultado

def main() -> None:
    numeros_originales = leer_numeros()
    numeros_factoriales = procesar_lista(numeros_originales)
    print(f"La lista de números originales: {numeros_originales}")
    print(f"La lista con los factoriales: {numeros_factoriales}")

if __name__ == "__main__":
    main()