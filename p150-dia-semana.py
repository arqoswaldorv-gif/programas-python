# p150-dia-semana.py
# Escribe un programa con una funcion que reciba un numero entero entre 1 y 7. La funcion debe devolver el dia de la semana correspondiente en texto (ej: 1 = "Lunes", 7 = "Domingo"). El programa principal debe pedir el numero al usuario, llamar a la funcion y mostrar el nombre del dia


def dia_semana(num: int) -> str:
    if num == 1:
        return "Lunes"
    elif num == 2:
        return "Martes"
    elif num == 3:
        return "Miercoles"
    elif num == 4:
        return "Jueves"
    elif num == 5:
        return "Viernes"
    elif num == 6:
        return "Sabado"
    elif num == 7:
        return "Domingo"
    else: 
        return "Error: El numero debe estar entre 1 y 7"

def main() -> None:
    numero = int(input("Ingresa un numeor (entre 1 y 7): "))
    msj = dia_semana(numero)    
    print(msj)

if __name__ == "__main__":
    main()