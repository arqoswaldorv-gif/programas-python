# - p136-estacion-año.py

def estacion_año(mes:int) -> str:
    est=''
    if mes in [12,1,2]:
        est = 'Invierno'
    elif mes in [3,4,5]:
        est = 'Primavera'
    elif mes in [9,10,11]:
        est = 'Otoño'
    else:
        est ='Mes invalido'
    return est

print(f'El mes 1 corresponde a: {estacion_año(1)}')
print(f'El mes 10 corresponde a: {estacion_año(10)}')

print('Dame un numero de mes (1-12)')
mes = int(input())
print(f'La estacion del año para le mes de {mes} es: {estacion_año(mes)}')