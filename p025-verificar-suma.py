# p025-verificar-suma.py
# dados 3 numeros verifica si la suma de los dos primeros es igual a un tercer numero

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print("Verificador de suma : Es la suma de los dos primeros igual  al tercero ? ")
print("-" * 60)

n1 = int(input("Dame el primer numero ? "))
n2 = int(input("Dame el segundo numero ? "))
n3 = int(input("Dame el tercer numero ? "))

suma = n1 + n2

if suma == n3 : 
    print(f" ✅ ¡Correcto! La suma de {n1} + {n2} es igual a {n3}")
else:
    print(f"\n ❌ No coincide. La suma de {n1} + {n2} es {suma}, lo cual es distinto de {n3}.")

print("-"*60)
print("Fin del programa.")   