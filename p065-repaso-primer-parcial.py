# p065-SistemaPapeleria.py

"""
Objetivo: Programa para calcular y registrar las ventas de una papeleria
Autor   : Oswaldo Rodriguez Vargas
Fecha   : 26 de Febrero del 2026

Planteamiento del problema:
   Una papelería necesita un programa para gestionar eficientemente el control de sus ventas de fotocopias. El sistema debe ser capaz de registrar múltiples ventas, calcular los subtotales por tipo de copia y el total general. Además, deberá clasificar el desempeño de las ventas del día con un mensaje descriptivo.

Tabla de Precios:
 • Carta (C): $3.00
 • Oficio (O): $4.00
 • Doble Oficio (D): $6.00
 • Plano (P): $12.00

Nueva Funcionalidad: Descuento por Volumen Para incentivar las compras grandes, se aplicará un descuento del 10% sobre el total de la venta si la cantidad de copias en una sola transacción es superior a 50 unidades, sin importar el tipo.

 Resumen de Ventas y Mensajes de Desempeño: Al finalizar el registro de ventas, el programa debe mostrar un resumen detallado. Basado en el monto total vendido, se mostrará uno de los siguientes mensajes:
 • Venta Moderada: Si el total es menor a $50.00.
 • Venta Frecuente: Si el total está entre $50.00 y $150.00.
 • Venta Superada: Si el total es mayor a $150.00.
"""

ventas = cantidad = subtotal = 0
cantidad_c = cantidad_o = cantidad_d = cantidad_p = 0
total_c = total_o = total_d = total_p = 0 

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
while True:
    ventas += 1
    print('-'*60)
    print(f'\nVenta {ventas}')
    
    print('Tipo de Copia:')
    print('(C)arta  $3')
    print('(O)ficio $4')
    print('(D)oble  $5')
    print('(P)lano  $12')
    tipo = input('Respuesta: ').upper()
    
    if tipo not in 'CODP':
        err = input('>>>>Error Tipo de copia no valido Intente de nuevo, <Enter>')
        ventas -=1
        continue
    
    cantidad = int(input('Cantidad? '))
    descuento = 1
    if cantidad > 50:
        descuento = 0.90
        print('** Descuetno del 10% aplicado por volumen de venta *** ')
        
    if tipo=='C':
        cantidad_c += cantidad
        subtotal = (cantidad * 3) * descuento
        total_c += subtotal
    elif tipo == 'O':
        cantidad_o += cantidad
        subtotal = (cantidad * 4) * descuento
        total_o += subtotal
    elif tipo == 'D':
        cantidad_d += cantidad
        subtotal = (cantidad * 6) * descuento
        total_d += subtotal
    elif tipo == 'P':
        cantidad_p += cantidad
        subtotal = (cantidad * 12) * descuento
        total_p += subtotal
    
    if input('\n¿Deseas ingresar otra venta (S/N)? ').upper() !='S': break

total_copias = cantidad_c + cantidad_o + cantidad_d + cantidad_p
total_ventas = total_c + total_o + total_d + total_p

print('-'*60)
print('Resumne diario de ventas')
print('-'*60)
print(f'Ventas realizadas: {ventas}')
print('-'*60)
print(f'Carta\t\t: {cantidad_c:2d} = $ {total_c:8.2f}')
print(f'Oficio\t\t: {cantidad_o:2d} = $ {total_o:8.2f}')
print(f'Doble Oficio\t: {cantidad_d:2d} = $ {total_d:8.2f}')
print(f'Plano\t\t: {cantidad_p:2d} = $ {total_p:8.2f}')
print('-'*60)
print(f'Total Ventas\t: {total_copias:2d} = $ {total_ventas:8.2f}')

mensaje_venta = ""
if total_ventas > 150:
    mensaje_venta = "Venta superada"
elif total_ventas >=50:
    mensaje_venta = "Venta Frecuente"
else:
    mensaje_venta = "Venta Moderada"
print(f'Esta venta es una venta : {mensaje_venta}')

print('Fin de las ventas por este dia')