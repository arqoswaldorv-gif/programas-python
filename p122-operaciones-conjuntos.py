# p122-operaciones-conjuntos.py
# Mostrar operaciones entre conjuntos

c1 = {1, 2, 3, 4, 5}
c2 = {5, 6, 7, 8, 9, 10}
c3 = {9, 10, 11, 12, 13}
c4 = {3, 4, 5}

print('\033[H\033[J')
print(f"c1:{c1}\nc2:{c2}\nc3:{c3}\nc4:{c4}")

print('\nUnion:')
print(f'c1 union c2: { c1.union(c2) }')
print(f'c1 union c3: { c1 | c3 }')

print('\nInterseccion')
print(f'c1 interseccion c2: { c1.intersection(c2) }')
print(f'c2 interseccion c3: { c1 & c3 }')

print('\nDiferencia')
print(f'c1 diferencia c4: elem c1 no en c4 { c1.difference(c4) }')
print(f'c2 diferencia c3: elem c2 no en c3 { c1 - c3 }')

print('\nDiferencia Simetrica')
print(f'c1 dif sim c2: elem en c1 o c2 no en ambos { c1.symmetric_difference(c2) }')
print(f'c2 dif sim c3: elem en c2 o c3 no en ambos { c2 ^ c3 }')

print('\nSUperconjuntos')
print(f'c1 es super conj de c4 ? : { c1.issuperset(c4) }')
print(f'c2 es super conj de c3 ? : { c2 >= c3 }')

print('\nSubconjuntos')
print(f'c1 es sub conj de c4 ? : { c1.issubset(c4) }')
print(f'c2 es sub conj de c3 ? : { c2 <= c3 }')

print('\nPertenencia  o no pertenencia a un conjunto')
print(f'Esta 2 en c1 ? : { 2 in c1 }')
print(f'No Esta 6 en c1 ? : { 6 not in c1 }')