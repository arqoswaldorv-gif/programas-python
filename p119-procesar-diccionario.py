# p119-procesar-diccionario.py
# • Define dos listas:
    # o nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
    # o sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]
# • Crea un diccionario nomina combinando ambas listas (los nombres son las llaves, los sueldos son los valores).
# • Muestra el diccionario nomina resultante.
# • Itera sobre el diccionario y muestra su contenido de cuatro formas:
    # o Mostrando solo las llaves (usando keys()).
    # o Mostrando solo los valores (usando values()).
    # o Iterando por las llaves y accediendo al valor (ej. for llave in dic: ...).
    # o Mostrando la llave y el valor simultáneamente (usando items()).
# • Calcula y muestra la suma total de los sueldos.
# • Calcula y muestra el promedio de los sueldos.

print('\033[H\033[J')

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

nomina = dict(zip(nombres,sueldos))

print('Diccionario de nomina:')
print(nomina)

print('\n--- Iterando Llaves (keys)')
for k in nomina.keys():
    print(k)

print('\n--- Iterando Valores (values)')
for v in nomina.values():
    print(v)

print('\n--- Iterando Llave y Valor (accediendo por llave)')
for k in nomina.keys():
    print(f'{k} -> {nomina[k]}')

print('\n--- Iterando Llave y Valor (items)')
for k, v in nomina.items():
    print(f'{k} -> {v}')
    
print('\n--- Calculos ---')
print(f'Suma total de sueldos: {sum(nomina.values())}')
print(f'Promedio de sueldos: {sum(nomina.values()) / len(nomina.keys()) :.2f}')