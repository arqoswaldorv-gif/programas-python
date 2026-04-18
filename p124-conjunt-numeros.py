# p124-conjunt-numeros.py


# Dadas las siguientes tres listas de números:
c1 = {50, 60, 70, 80, 90, 100, 200}
c2 = {60, 90, 100, 300, 400, 500}
c3 = {10, 20, 60, 90, 70, 100, 600, 700}

print('\033[H\033[J')
print("--- Gestion de nombres (usando conjuntos) ---")

# Instrucciones:
# 1. Crear y mostrar los conjuntos A, B y C a partir de las listas.
print(f"c1:{c1}\nc2:{c2}\nc3:{c3}")

# 2. Calcular y mostrar los resultados de las siguientes operaciones:
# o Unión (A | B)
print(f'\nUnion (A|B): { c1.union(c2) }')

# o Unión (B | C)
print(f'\nUnion (B|C): { c2.union(c3) }')

# o Diferencia (A - C)
print(f'\nDiferencia (A|C): { c1.difference(c3) }')

# o Diferencia Simétrica (B ^ C)
print(f'\nDif Sim (B^C): { c2.symmetric_difference(c3) }')

# o Intersección (B & C)
print(f'\nInterseccion (B&C): { c2.intersection(c3) }')


# 3. Verificar y mostrar el resultado (Verdadero/Falso) de las siguientes preguntas:
# o ¿Es A subconjunto de B?
print(f'\n¿Es A subconjunto de B? : { c1.issubset(c2) }')

# o ¿Es C subconjunto de A?
print(f'\n¿Es C subconjunto de A? : { c3.issubset(c1) }')

# o ¿Está el número 100 en A?
print(f'\n¿Está el número 100 en A? : { 100 in c1}')

# o ¿Está el número 60 en A, B y C?
print(f'\n¿Está el número 60 en A, B y C? : { 60 in c1 and 60 in c2 and 60 in c3}')

# o ¿No está el número 900 en C?
print(f'\n¿Está el número 900 en C? : { 900 not in c3 }')