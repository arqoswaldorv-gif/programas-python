# p159-rectangulo.py
# Modela un rectangulo

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def obtenerArea(self):
        return self.largo * self.ancho
    def obtenerPerimetro(self):
        return 2 * self.largo * self.ancho
    def __str__(self):
        return f"Rectangulo[ Largo={self.largo}, Ancho={self.ancho}, Area={self.obtenerArea():.2f},Perimetro:{self.obtenerPerimetro():.2f}]"
    

print("\033[H\033[J")
r1 = Rectangulo(12, 3.4)
print(f"\nPrimer {r1}")

r2 = Rectangulo(5.6, 7.8)
print(f"\nSegundo {r2}")

r3 = Rectangulo(10, 20)
print(f"\nTercer {r3}")

print(f"\nPromedio de areas: { (r1.obtenerArea() + r2.obtenerArea() + r3.obtenerArea()) /3 }")