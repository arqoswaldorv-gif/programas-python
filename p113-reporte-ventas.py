# p113-reporte-ventas.py
# Crear un diccioanrio de diccioanrios

print('\033[H\033[J')
print('Reporte de Ventas por Cliente\n')

n = int(input('Numero de compras a Registrar: '))
compras = []

for i in range(n):
    print(f'\n----- Compra {i+1} ------')
    compra ={
        'cliente' : input('Cleinte : '),
        'producto' : input('Producto: '),
        'cantidad' : float(input('Cantidad : ')),
        'precio' : float(input('Precio : '))
    }
    compras.append(compra)

print('\nLista de compras registradas')
print(compras)

clientes = {}
for compra in compras:
    cliente = compra['cliente']
    if cliente not in clientes:
        clientes[cliente] = {"cantidad": 0, "subtotal": 0}
    
    clientes[cliente]['cantidad'] += compra['cantidad']
    clientes[cliente]['subtotal'] += compra['cantidad'] * compra['precio']

# print(clientes)

for cliente, datos in clientes.items():
    print(f'Cliente: {cliente}')
    print(f'Cantidad: {datos['cantidad']}')
    print(f'Subtotal: {datos['subtotal']}')
    print()