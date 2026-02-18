# p034-tipo-angulo.py
# Mostrar el tipo de angulo en base a su magnitud

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('-- Clasificacion de Angulos --')

angulo = int(input('Dame un angulo en grados ? '))

if angulo >= 0 and angulo <= 360:
    if angulo < 90:
        print(f'El angulo de {angulo} grados es un angulo AGUDO')
    elif angulo == 90:
        print(f'El angulo de {angulo} grados es un angulo RECTO')
    elif angulo < 180:
        print(f'El angulo de {angulo} grados es un angulo OBTUSO')
    elif angulo == 180:
        print(f'El angulo de {angulo} grados es un angulo LLANO')
    elif angulo < 360:
        print(f'El angulo de {angulo} grados es un angulo CONCAVO')
    else:
        print(f'El angulo de {angulo} grados es un angulo COMPLETO O CERRADO')
else:
    print(f"Angulo fuera de rango")        
        
print('\nProceso terminado')