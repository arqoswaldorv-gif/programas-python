# p098-producto-punto.py
# Calcula el punto de 2 vectores 

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Calcular el putno de dos vectores')

A = [1,  3, -5]
B = [4, -2, -1]
C = []

print(f'Vector A: {A}')
print(f'Vector B: {B}')

if len(A) == len(B):
    print('Calculando el producto punto ...')
    for i in range(len(A)):
        producto = A[i] * B[i]
        C.append(producto)
        
    print(f'Vector C: {C}')
    print(f'El producto punto es : {sum(C)}')
else:
    print("Los vectores deben ser del mismo tamaño")