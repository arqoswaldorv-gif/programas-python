# p151–medidas-longitud.py
# Desarrolla un programa que funcione como un conversor de unidades de longitud. El programa debe mostrar un manu y utilziar dos funciones separadas:
# 1.- Una funcion para convertir pulgadas a centimetros (formula: $cm = pulgadas \times 2.54$)
# 2.- Una funcion para convertir metros a pies (formla: $pies = metros \times 3.281$)
# El programa debe solicitar los datos al usuario segun la opcion elegida y mostrar el resultado


def pulgadas_centimetros() -> None:
    pulgadas = float(input("Ingresa las pulgadas: "))
    centimetros = pulgadas * 2.54
    print(f"{pulgadas} pulgadas = {centimetros:.2f} centimetros")

def metro_pies() -> None:
    metros = float(input("Ingresa los metros: "))
    pies = metros * 3.281
    print(f"{metros} metros = {pies:.2f} pies")



def main() -> None:
    aux = True
    while aux:
        print("*** Conversor de Unidades ***")
        print("1.- Pulgadas a Centimetros")
        print("2.- Metros a Pies")
        print("3.- Salir")
        op = int(input("Elige una opcion: "))
        
        if op == 1:
            pulgadas_centimetros()
        
        elif op == 2:
            metro_pies()
        
        elif op == 3:
            aux = False

if __name__ == "__main__":
    main()