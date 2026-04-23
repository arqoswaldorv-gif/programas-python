# p125-segundo-examen-parcial.py

"""
 Nombre del Alumno: Oswaldo Rodriguez Vargas
 Matrícula: 31123924
 Materia: Computación Aplicada
 Examen: Segundo Parcial
  Objetivo: Se desea procesar el registro de vuelos de una aerolínea ("AeroRegistro"). Para ello,
deberá solicitar al usuario los siguientes datos por cada vuelo:
    • numero_vuelo (identificador del vuelo, ej. 'AA-101')
    • origen (ciudad de salida, ej. 'Ciudad de México')
    • destino (ciudad de llegada, ej. 'Guadalajara')
    • aerolinea (nombre de la aerolínea, ej. 'AeroMéxico', 'Volaris', 'Interjet')
    • pasajeros (número de pasajeros a bordo, ej. 180)
    • tarifa (precio del boleto en pesos, ej. 2350.75)
 Los datos se deben almacenar en una lista, donde cada elemento de la lista sea un diccionario con los
datos de un vuelo.
 Nota: No olvides documentar las partes importantes del código, explicando que hace ese fragmento de
código en específico.
"""

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos

# --- Lista de Vuelos ---
# Almacenaremos cada vuelo como un diccionario dentro de esta lista
vuelos = []


print('\033[2J\033[H')
print("--- AeroRegistro - Sistema de Vuelos ---")

# --- Ciclo Principal para registro de Vuelos ---
# Usaremos un ciclo while para registrar vuelos hasta que el usuario ingrese un número de vuelo vacío.
print("\nCaptura de datos de los vuelos (* para terminar):")
while True:

    print("\n--- Nuevo Vuelo ---")
    # --- 1. Solicitud de Datos ---
    # Pide numero_vuelo, origen, destino, aerolinea, pasajeros, tarifa.
    numero_vuelo = input("Introduce el número de vuelo (* para terminar): ")
    if numero_vuelo == "*":
        break

    datos = {}
    datos['numero_vuelo'] = numero_vuelo
    datos['origen'] = input("Introduce la ciudad de origen: ")
    datos['destino'] = input("Introduce la ciudad de destino: ")
    datos['aerolinea'] = input("Introduce la aerolínea: ")
    datos['pasajeros'] = int(input("Introduce el número de pasajeros: "))
    datos['tarifa'] = float(input("Introduce la tarifa del boleto: "))
    vuelos.append(datos)

# --- FIN DEL CICLO ---


# --- 1. Datos Crudos ---
print(('\n--- Datos (Lista de Diccionarios) ---'))
print(vuelos)

# --- 2. Datos Tabular ---
print(('\n--- Tabla de Datos ---'))
print(' No. Vuelo \t| Origen \t\t| Destino \t| Aerolínea \t| Pasajeros \t| Tarifa ')
for vuelo in vuelos:
    print(f'{vuelo['numero_vuelo']} \t\t| {vuelo['origen']} \t\t| {vuelo['destino']} \t| {vuelo['aerolinea']} \t| {vuelo['pasajeros']} \t\t| {vuelo['tarifa']:,.2f} ')

# --- 3. Resumen del Registro ---
print('\n--- RESUMEN ---')
print(f'Vuelos totales: {len(vuelos)}')


# --- 3.1. Contador de Aerolíneas ---
# Contamos cuántos vuelos hay por cada aerolínea
aerolineas = {}
for vuelo in vuelos:
    aerolinea = vuelo['aerolinea']
    if aerolinea not in aerolineas:
        aerolineas[aerolinea] = {"nombre": aerolinea, "cantidad": 0}

    aerolineas[aerolinea]['cantidad'] += 1


print('\nAerolíneas: ')
# Iteramos sobre los valores del diccionario para acceder a cada aerolínea
for aerolinea in aerolineas.values():
    print(f'- {aerolinea['nombre']}: {aerolinea['cantidad']}')

# --- 3.2. Contador de Destinos ---
# Contamos cuántos vuelos hay por cada ciudad de destino
destinos = {}
for vuelo in vuelos:
    destino = vuelo['destino']
    if destino not in destinos:
        destinos[destino] = {"nombre": destino, "cantidad": 0}

    destinos[destino]['cantidad'] += 1


print('\nDestinos: ')
# Iteramos sobre los valores del diccionario para acceder a cada destino
for destino in destinos.values():
    print(f'- {destino['nombre']}: {destino['cantidad']}')

suma_pasajeros = sum(v['pasajeros'] for v in vuelos)
promedio_pasajeros = suma_pasajeros / len(vuelos) if len(vuelos) > 0 else 0
print(f"\n- Pasajeros -> Suma: {suma_pasajeros}, Promedio: {promedio_pasajeros:.1f}")

suma_tarifa = sum(v['tarifa'] for v in vuelos)
promedio_tarifa = suma_tarifa / len(vuelos) if len(vuelos) > 0 else 0
print(f"\n- Tarifa -> Suma: {suma_tarifa:,.2f}, Promedio: {promedio_tarifa:,.2f}")


vuelo_mas_caro = max(vuelos, key=lambda v: v['tarifa'])
vuelo_mas_barato = min(vuelos, key=lambda v: v['tarifa'])
print(f"\n- {vuelo_mas_caro['numero_vuelo']} de ${vuelo_mas_caro['tarifa']:,.2f} es el más caro, {vuelo_mas_barato['numero_vuelo']} de ${vuelo_mas_barato['tarifa']:,.2f} es el más barato.")