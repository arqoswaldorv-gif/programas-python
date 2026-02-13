# p026-convertir-temperaturas-v2.py
# Convertir de Celsius a Farenheit y viceversa

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print("conversion de tempraturas \n")

print("[1] de Farenheit a Celsius")
print("[2] de Celsius a Farenheit")

opcion = int(input("Elige una opcion ?"))

if opcion==1:
    print("\nConversion a Celsius...")
    f = float(input("Dame los Farenheit ?"))
    c = (f - 32) * 5 / 9
    print(f"{f} grados Farenheit, equivale a {c:.2f} grados Celsius")
elif opcion==2:
    print("\nConversion a Farenheit...")
    c = float(input("Dame los Celsius ?"))
    f = (c * 5 / 9) + 32
    print(f"{f} grados Celsius, equivale a {f:.2f} grados Farenheit")
else:
    print("\nLa opcion no es valida")
print("\nPrograma Finalizado")