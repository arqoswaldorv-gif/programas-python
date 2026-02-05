# p006-conversor-temperatura.py
# Convertir temperatura de grados Celsius a Farenheit

print("Convirtiendo grados Celcius a grados Fahrenheit: /n")

Celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = (Celsius * 9/5) + 32

print(f"La temperatura en Fahrenheit es:{fahrenheit:.2f} °F")