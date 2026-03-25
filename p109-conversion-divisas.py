# p109-conversion-divisas.py
# Conversor de divisas a pesos mexicanos

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Conversor de divisas a pesos mexicanos')

conv = {
    'USD': 20.50,
    'EUR': 22.30,
    'GBP': 25.80,
    'JPY': 0.19,
    'CAD': 16.20
}

print('\Opciones de cambio de moneda a pesos mexicanos MXM')

for m in conv:
    print(f'- {m}')

while True:
    moneda = input('\nIngresa la moneda a convertir : ').upper()
    if moneda in conv: break
    continue

while True:
    try: 
        cant = float(input(f'Ingresa la cantidad en {moneda}: '))
        if cant > 0 : break
    except:
        print('Entrada no valida')

res = cant * conv[moneda]

print(f'{cant:,.2f} {moneda} equivale a {res:,.2f} MXN')