# p077-triangulo-caracter.py
# Imprime un triangulo rectangulo de n reglones del caracter deseado

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print("--- Imprime un triangulo rectangulo de n reglones del caracter deseado ---")

n = int(input("Renglones ? "))
c = input("Caracter  ? ")

# EL bucle exteriro se ejecuta N veces
for i in range(1, n + 1):
    # Por cada iteracion del bucle exterior, el bucle interior se ejecuta M veces
    for j in range(1, i):
        #Aqui se ejecutan las acciones anidadas
        print(f"{c}", end='')
        
    print()