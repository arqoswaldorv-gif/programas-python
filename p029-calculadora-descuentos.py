# p029-calculadora-descuentos.py
# Simula una calculadora de descuentos basada en el monto de la compra

print("\033[2J\033[H")
print("Calculadora de descuentos ")

descuento = 0
porcentaje = 0

compra = float(input(" Ingresa el total de la compra ? "))

if compra > 2000:
    porcentaje = 0.20
elif compra > 1000:
    porcentaje = 0.10
elif compra > 500:
    porcentaje = 0.05
else :
    porcentaje = 0

descuento = compra * porcentaje
total = compra - descuento

print("\nResumen")
print(f"Total de la compra: $ {compra:,.2f}")
print(f"Porcentaje de desc: $ {porcentaje*100:,.2f}%")
print(f"Ahorro            : $ {descuento:,.2f}")
print(f"total a pagar     : $ {total:,.2f}")