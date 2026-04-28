# p145-mayores-promedio.py

from typing import List

def promedio_lista(lista:List[float]) -> float:
    suma = 0
    if not lista:
        return 0.0
    for numero in lista:
        suma += numero
    return suma / len(lista)

def mayoers_promedio(lista:List[float], promedio: float) -> List[float]:
    mayores: List[float] = []
    for numero in lista:
        if numero > promedio:
            mayores.append(numero)
    return mayores

def main() -> None:
    numeros : List[float] = [1.5, 2.3, 3.7, 4.0, 5.5]
    promedio = promedio_lista(numeros)
    resultado = mayoers_promedio(numeros, promedio)
    print(f'El promedio es : {promedio}')
    print(f'Numeros mayores al promedio: {resultado} - {len(resultado)}')
    
if __name__ == "__main__":
    main()