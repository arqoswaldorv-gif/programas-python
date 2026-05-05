# p158-circulo.py
# Modelamos un circulo , usando una clase
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def obtenerArea(self):
        return math.pi * math.pow(self.radio,2)
    def obtenerCircunferencia(self):
        return 2 * math.pi * self.radio
    def __str__(self):
        return f"Circulo [ Radio = {self.radio}, Area = {self.obtenerArea()}, Circunferencia: {self.obtenerCircunferencia():.2f}]"
    
print("\033[H\033[J")

circulo1 = Circulo(10.40)
print(circulo1)
print(f"Area            : {circulo1.obtenerArea():.2f}")
print(f"Circunferencia  : {circulo1.obtenerCircunferencia():.2f}\n")

circulo2 = Circulo(12.45)
print(circulo2)
print(f"Area            : {circulo2.obtenerArea():.2f}")
print(f"Circunferencia  : {circulo2.obtenerCircunferencia():.2f}\n")