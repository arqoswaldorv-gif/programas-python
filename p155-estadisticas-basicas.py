# p155-estadisticas-basicas.py
# Crea un programa que calcule estadisticas basicas (poblacionales) para una lista de numeros. El programa debe incluir
# 1.- Una funcion para leer una lista de nuemro enteros
# 2.- Funciones separadas para calcular y devolver cada una de als siguietnes estadisticas
# o Número mayor
# o Número menor
# o Media (promedio)
# o Varianza poblacional
# o Desviación estándar poblacional
# El programa principal debe leer la lista e imprimir todos los resultados estadisticas de forma clara

from typing import List

def leer_numeros() -> List[int]:
    entrada = input("Dame números (separados por espacio): ")
    numeros_str = entrada.split()
    numeros: List[int] = []
    for num_str in numeros_str:
        numeros.append(int(num_str))
    return numeros

def mayor(lista: List[int]) -> int:
    num_mayor = lista[0]
    for numero in lista:
        if numero > num_mayor:
            num_mayor = numero
    return num_mayor

def menor(lista: List[int]) -> int:
    num_menor = lista[0]
    for numero in lista:
        if numero < num_menor:
            num_menor = numero
    return num_menor

def media(lista: List[int]) -> float:
    suma = 0
    if not lista:
        return 0.0
    for numero in lista:
        suma += numero
    return suma / len(lista)

def varianza(lista: List[int]) -> float:
    if not lista:
        return 0.0
    promedio = media(lista)
    suma_cuadrados = 0
    for numero in lista:
        diferencia = numero - promedio
        suma_cuadrados += diferencia * diferencia
    return suma_cuadrados / len(lista)

def desviacion_estandar(lista: List[int]) -> float:
    var = varianza(lista)
    return var ** 0.5

def main() -> None:
    numeros = leer_numeros()
    print(f"Lista de números: {numeros}")
    print("Estadísticas:")
    print(f"Media              : {media(numeros):.3f}")
    print(f"Mayor              : {mayor(numeros)}")
    print(f"Menor              : {menor(numeros)}")
    print(f"Varianza           : {varianza(numeros):.3f}")
    print(f"Desviación estándar: {desviacion_estandar(numeros):.3f}")

if __name__ == "__main__":
    main()