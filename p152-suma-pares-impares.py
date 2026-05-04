# p152-suma-pares-impares.py
# Crea un porgrama que sume numero pares o impares dentro de un rango especificado. El programa debe tener una funcion que reciba tres parametros: un numero de inicio, un numero de fin y una letra ('P' o 'I')
# Si la letra es 'P', la funcion debe devolver la suma de todos los numeros pares en ese rango (incluyendo los limites)
# Si la letra es 'I', la funcion debe devolver la suma de todos los nuemros imapres en el rango
# El programa principal debe mostrar un menu, pedir los datos al usuario y mostrar el resultado de la suma


def par_impar(n_inicio: int, n_fin: int, op: str) -> int:
    suma = 0
    tipo_numero = ""
    numeros = []
    
    for i in range(n_inicio, n_fin + 1):
        if op == "P" and i % 2 == 0:
            suma += i
            numeros.append(i)
        elif op == "I" and i % 2 != 0:
            suma += i
            numeros.append(i)
    
    if op == "P":
        tipo_numero = "pares"
    elif op == "I":
        tipo_numero = "impares"
    
    print(f"La suma de los numeros {tipo_numero} entre {n_inicio} y {n_fin} es: {suma}")
    print(f"(Cálculo: {numeros} = {suma})")
    return suma




def main() -> None:
    print('*** suma en Rango ***')
    n_inicial = int(input("Introduce el numero inicial: "))
    n_final = int(input("Introduce el numero final: "))
    op = input("¿Que deseas sumar? (P)ares o (I)mpares ").upper()
    
    par_impar(n_inicial, n_final, op)
    

if __name__ == "__main__":
    main()
    
    
    """
    Ejemplo de Ejecución:
*** Suma en Rango ***
Introduce el número inicial: 5
Introduce el número final: 15
¿Qué deseas sumar? (P)ares o (I)mpares: P
La suma de los números pares entre 5
(Cálculo: 6 + 8 + 10 + 12 + 14 = 50)
    """