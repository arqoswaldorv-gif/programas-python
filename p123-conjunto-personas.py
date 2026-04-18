# p123-conjunto-personas.py
# Dadas las siguientes dos listas de nombres:
lista1 = {'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'}
lista2 = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}

print('\033[H\033[J')
print("--- Gestion de nombres (usando conjuntos) ---")

# Instrucciones:
# 1. Crear y mostrar los conjuntos A (basado en la Lista 1) y B (basado en la Lista 2).
print('Datos uno a uno de lista 1:')
for nombre in lista1:
    print(nombre, end=' | ')

print('\n\nDatos uno a uno de lista 2:')
for nombre in lista2:
    print(nombre, end=' | ')

print()
# 2. Calcular y mostrar los resultados de las siguientes operaciones:
# o Unión (A | B)
print(f'\nUnion (A|B): { lista1.union(lista2) }')

# o Intersección (A & B)
print(f'\nInterseccion (A&B): { lista1.intersection(lista2)}')

# o Diferencia (A - B)
print(f'\nDiferencia (A - B): { lista1.difference(lista2)}')

# o Diferencia Simétrica (A ^ B)
print(f'\nDif Sim (A ^ B): { lista1.symmetric_difference(lista2)}')


# 3. Verificar y mostrar el resultado (Verdadero/Falso) de las siguientes afirmaciones:
# o ¿Es {Pablo, Mateo} un subconjunto de B?
print(f'\n¿Es {{Pablo, Mateo}} un subconjunto de B?: { {"Pablo", "Mateo"}.issubset(lista2)}')

# o ¿Es A un superconjunto de {Reynaldo, Angelica}?
print(f'¿Es A un superconjunto de {{Reynaldo, Angelica}}?: { lista1.issuperset({"Reynaldo", "Angelica"}) }')

# o ¿Está "Pedro" en el conjunto A?
print(f'¿Está "Pedro" en el conjunto A?: { "Pedro" in lista1 }')

# o ¿No está "Lilia" en el conjunto B?
print(f'¿No está "Lilia" en el conjunto B?: { "Lilia" not in lista2 }')