# p004-paga-trabajador.py
# Calcula la paga de un trabajador

print("Calculando la paga de un trabajador")
# Entrada
nombre = input("Nombre >")
horas = int(input("Horas trabajadas >"))
paga = float(input("Paga x hora"))
# Proceso
tasa = 0.3
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto
# Salida
print(f"El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga} pesos, impuesto de {tasa} %")
print(f"Paga Bruta : {pagabruta}")
print(f"Impuesto. : {impuesto}")
print(f"Paga Neta : {paganeta}")