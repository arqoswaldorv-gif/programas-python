# p027-calcular-paga-extra-v2.py
# Calcula la paga de un trabajador considerando horas extra.

print("\033[2J\033[H")
print('Calculando la paga de un trabajador considerando las horas extra (se considera al doble) \n')

print("Dame los datos del trabajador:\n")
nombre = input("Nombre : ")
horas = int(input("horas : "))
paga_hora = float(input("Paga por hora: "))

if horas < 40:
    horas_normales = horas
else:
    horas_normales = 40

paga_normal = horas_normales * paga_hora

horas_extra = paga_extra = 0

if horas > 40:
    horas_extra = horas - 40
    paga_extra = horas_extra * (paga_hora * 2)
    total = paga_normal + paga_extra
else:
    total = paga_normal

print("\nCalculo completado :")
print(f"\nEl trabajador {nombre} trabajo {horas} horas, con una paga de {paga_hora} pesos")
print(f"Trabajo {horas_extra} horas extra")
print(f"Paga normal: $ {paga_normal:13,.2f}")
print(f"Paga extra: $  {paga_extra:13,.2f}")
print(f"Paga Total : $ {total:13,.2f}")