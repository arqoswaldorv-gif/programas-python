# p012-funcion-matematicas-equacion.py
# Evaluar la funcion f(x, y) =  3x² + √(x² + y²) + e^(ln(x))
# Usando operadores de exponenciacion y la funcion pow

import math as mt

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

print("Evaluar la expresion: f(x, y) =  3x² + √(x² + y²) + e^(ln(x) 😁")
x= float(input("Dame X : "))
y= float(input("Dame Y : "))
fxy = 3 * mt.pow(x,2) + mt.sqrt(mt.pow(x,2) + mt.pow(y,2)) +  mt.exp( mt.log(x)) 

print(f" El resultado de f({x},{y})= {fxy:.2f}")