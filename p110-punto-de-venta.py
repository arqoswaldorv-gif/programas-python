# p110-punto-de-venta.py
# Simular un punto de venta

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Simuladno un punto de venta')

menu = {
    'taco': 18.50,
    'burrito': 45,
    'Quesadilla': 35,
    'refresco': 20.00,
    'agua': 15
}

print('\n---- Bienvenido al Taco Feroz ----')
print('Este es nuestro menu: ')
for a, p in menu.items():
    print(f' - {a:<12} : ${p:,.2f}')

orden = {}
total_general = 0

while True:
    producto = input('\nQue deseas ? ').lower()
    if producto == 'fin': break
    cantidad = int(input('Cantidad: '))
    orden[producto] = orden.get(producto,0) + cantidad
    print(f'Agregados {cantidad} {producto} a tu orden')

print(f'Tu orden fue :\n {orden}')
print('\n--- RECIBO ---')
if not orden:
    print('No compraste nada')
else:
    for p, c in orden.items():
        precio_unitario = menu[p]
        subtotal = precio_unitario * c
        print(f'{c} X {p:<12} : ${subtotal:,.2f}')
        total_general += subtotal

print('-'*35)
print(f'TOTAL A PAGAR: $ {total_general:,.2f}')
print('Gracias por tu compra')