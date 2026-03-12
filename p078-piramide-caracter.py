# p078-piramide-caracter.py
# Imprime una piramide de caracteres

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print("--- Imprime una piramide de caracteres ---")

n = int(input("Renglones ? "))
c = input("Caracter  ? ")

# EL bucle exteriro se ejecuta N veces
for i in range(1, n + 1):
    espacios = n - i
    for k in range(espacios):
        print(' ', end='')
        
    caracteres = 2 * i - 1
    # Por cada iteracion del bucle exterior, el bucle interior se ejecuta M veces
    for j in range(caracteres):
        #Aqui se ejecutan las acciones anidadas
        print(f"{c}", end='')
        
    print()