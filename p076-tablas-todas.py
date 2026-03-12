# p076-tablas-todas.py
# Imprime todas la tablas de 1 a n, hasta m

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print("--- Imprimiendo la tabla de Multiplicar de 1 a n, hasta m ---")

n = int(input("Hasta que tabla        ? "))
m = int(input("Hata que multiplicador ? "))

# EL bucle exteriro se ejecuta N veces
for i in range(1, n + 1):
    print(f'\n--- Tabla del {i}')    
    # Por cada iteracion del bucle exterior, el bucle interior se ejecuta M veces
    for j in range(1, m + 1):
        #Aqui se ejecutan las acciones anidadas
        print(f"{i} x {j} = {i * j}")
        
    print('\n')