# p153-suma-digitos.py
# Escribe un porgrama que procese una lista de numeros. Debes implemetar lo sigueinte:
# 1.- Una funcion que lea y devuelva una lista de numeros enteros (puedes reusar la hecha en clase)
# 2.- Una funcion que reciba un numeor entero y devuelva la suam de sus digitos individuales (ej> 1971 -> 1 + + 7+1 =18)
# 3.- Una funcion principal que reciba la lista de nuemros. Esta debe usar la funcion anterior para crear y devolver una nueva lista que contenga la suam de los digitos de cad anuermo original
# El progarma debe imprimir la lista original y la nueva lista con las sumas

from typing import List

def leer_numeros() -> List[int]:
    entrada = input("Dame los números (separados por espacio): ")
    numeros_str = entrada.split()
    numeros: List[int] = []
    for num_str in numeros_str:
        numeros.append(int(num_str))
    return numeros

def suma_digitos(num: int) -> int:
    suma = 0
    for digito in str(num):
        suma += int(digito)
    return suma

def procesar_lista(lista: List[int]) -> List[int]:
    resultado: List[int] = []
    for numero in lista:
        suma = suma_digitos(numero)
        resultado.append(suma)
    return resultado

def main() -> None:
    numeros_originales = leer_numeros()
    numeros_suma = procesar_lista(numeros_originales)
    print(f"La lista de números original : {numeros_originales}")
    print(f"La lista con las suma de dígitos de los números: {numeros_suma}")

if __name__ == "__main__":
    main()