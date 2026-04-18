# p118-eliminar-diccionario.py
# • Crea un diccionario municipios con los datos: Apozol: 1863, Calera: 1868, Fresnillo: 1554, Guadalupe:
# 1821, Jalpa: 1824, Jerez: 1824, Loreto: 1931, Mazapil: 1824, Momax: 1857.
# • Muestra el diccionario inicial.
# • Realiza las siguientes eliminaciones, mostrando el estado del diccionario después de cada operación:
    # o Elimina Apozol (usando del).
    # o Elimina Fresnillo (usando pop()).
    # o Elimina el último elemento insertado (Momax) (usando popitem()).
# • Vacía el diccionario (usando clear()).
# • Muestra el diccionario final (vacío).

print('\033[H\033[J')

municipios = {
    'Apozol': 1863,
    'Calera': 1868,
    'Fresnillo': 1554,
    'Guadalupe': 1821,
    'Jalapa': 1824,
    'Jerez': 1824,
    'Loreto': 1931,
    'Mazapil': 1824,
    'Momax': 1857
}

print('Diccionario Inicial:')
print(municipios)

print("\nDespués de 'del Apozol':")
del municipios['Apozol']
print(municipios)

municipios.pop("Fresnillo")
print('\nDespués de "pop("Fresnillo")":')
print(municipios)

municipios.popitem()
print("\nDespués de 'popitem()' (eliminando Momax):")
print(municipios)

municipios.clear()
print("\nDespués de 'clear()': ")
print(municipios)