# p005-calculadora-imc.py
# Calcular el IMC de una persona

print("Calculando el indice de masa corporal (IMC) : /n")

peso_kg = float(input("Dame tu peso en Kilogramos:"))
altura_m = float(input("Dame tu altura en metros:"))

imc = peso_kg / altura_m ** 2 # El ** es un operador aritmetico que eleva u numero a una potencia

print(f" Si tienes un peso de {peso_kg} y una altura de {altura_m} tu IMC es {imc:.2f}")