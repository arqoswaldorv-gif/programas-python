# p067-conteo-ascendente-for.py
# Imprime numeros de 1 a 100 usadno un ciclo for

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print("--- Iniciando Secuencia ascendente ---")

for f in range(100,0,-1):
    print(f, end='')