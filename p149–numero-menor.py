# p149–numero-menor.py
# Crea un programa que incluya una funcion. Dicha funcion debe solicitar 3 numeros enteros al usuario y devolver el menor

def menor_de_3(n1:int, n2:int, n3:int) -> int:
    num_menor = n1
    if num_menor > n2:
        num_menor = n2
    if num_menor > n3:
        num_menor = n3
    return num_menor

def main() -> None:
    n1 = int(input("Introduce el primer numero: "))
    n2 = int(input("Introduce el primer numero: "))
    n3 = int(input("Introduce el primer numero: "))
    
    menor = menor_de_3(n1, n2, n3)
    
    print(f'El numero menor es: {menor}')
    

if __name__ == "__main__":
    main()