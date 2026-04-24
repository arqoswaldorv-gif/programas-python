# p140-promedio-letra.py

def cal_letra(prom: float) -> tuple[str, str]:
    let=''
    men=''
    if 90 <= prom <= 100:
        let='A'; men='Excelente'
    elif 80 <= prom <= 90:
        let='B'; men='Bien'
    elif 70 <= prom <= 80:
        let='C'; men='Suficiente'
    elif 60 <= prom <= 70:
        let='D'; men='Deficiente'
    elif 0 <= prom <= 60:
        let='F'; men='Reprobado'
    else:
        let=''; men='Calificacion invalida'
    
    return let,men

# l, m = cal_letra(59)
# print(f'Para un promedio de 59: corresponde: {l} - {m}')
    
def main() -> None:
    prom =float(input('Dame el promedio: '))
    letra, mensaje = cal_letra(prom)
    if letra:
        print(f'Calificacion {letra} - {mensaje}')
    else: 
        print(mensaje)


if __name__ == "__main__":
    main()