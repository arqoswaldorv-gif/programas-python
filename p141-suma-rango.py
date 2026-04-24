# p141-suma-rango.py
# Dado el inicio y fin, regrese la suma de numeros en el renago especificado

def suma_rango(inicio:int, fin:int) -> int:
    suma = 0
    for numero in range(inicio, fin + 1):
        suma += numero
    return suma

def main() -> None:
    inicio = int(input("Introduce el inicio del rango: "))
    fin = int(input("Introduce el fin del rango: "))
    resultado = suma_rango(inicio, fin)
    print(f"La suam de los numeros en el reango de {inicio} a {fin} es {resultado}")

    
if __name__ == " __main__":
    main()