# p066–primer-examen-parcial.py


"""
Objetivo: Un cine local necesita un programa para administrar la venta de boletos para una función especial en una de sus salas. EL programa debe controlar la venta de boletos, gestionar el aforo y calcular los ingresos generados. Diseña un porgrama en Python (en base a la plantilla anexa), aplicando los conocimietnos aprendidos en clase, para resolver el problema de acuerdo con los siguientes requisitos.
Nombre del Alumno: Oswaldo Rodriguez Vargas
Matrícula: 31123924
Materia: Computación Aplicada
Examen: Primer Parcial
"""

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos

# --- Contadores de Asistentes ---
total_estudiantes = 0
total_adulto = 0
total_tercera_edad = 0
total_academico = 0
total_asistentes = 0
total_rechazados = 0
total_hombres = 0
total_mujeres = 0
suma_edades = 0

# --- Acumuladores de Ingresos ---
ingresos_estudiantes = 0.0
ingresos_adultos = 0.0
ingresos_tercera_edad = 0.0
ingresos_academicos = 0.0
ingresos_totales = 0.0

# --- Precios de los Boletos (constantes) ---
PRECIO_ESTUDIANTE = 50.0
PRECIO_ADULTO = 90.0
PRECIO_TERCERA_EDAD = 60.0
PRECIO_ACADEMICO = 70.0

print('\033[2J\033[H')
print("--- Sistema de Venta de Boletos de Cine ---")

# --- Ciclo Principal para la Venta de Boletos ---
# Usaremos un ciclo while para registrar ventas hasta que el usuario decida parar.
continuar_venta = "s"
while continuar_venta == "s":

    print("\n--- Nueva Venta ---")
    # --- 1. Solicitud de Datos ---
    # Pide la edad, el tipo de comprador y el sexo.
    edad = int(input("Introduce la edad del comprador: "))
    
    # --- 2. Validación de Edad (Clasificación B) ---
    # La película es para mayores de 13 años.
    
    # Si la edad es permitida, procede con la venta.
    if edad > 13: 
        
        # Tipo de comprador y el sexo
        print('Tipo de Comprador:')
        print('1.-Estudiante')
        print('2.-Adulto')
        print('3.-Tercera Edad')
        print('4.-Académico')    
        comprador = int(input('Respuesta: '))
        sexo = input("Introduce tu sexo (H/M): ").upper()
        
        # Muestra el mensaje de bienvenida con los datos registrados
        print(f"¡Bienvenido(a)!... {edad} años, tipo de comprador {comprador}, sexo {sexo}.")
       
        
        # --- 3. Actualización de Estadísticas Generales ---
        # Incrementa el contador de asistentes y suma la edad para el promedio.
        total_asistentes += 1
        suma_edades += edad
        
        # Incrementa el contador de sexo correspondiente (hombre o mujer).
        if sexo == 'H':
            total_hombres += 1
        else: 
            total_mujeres += 1

        # --- 4. Cálculo de Costo y Actualización de Contadores Específicos ---
        # Usa una estructura if/elif/else para determinar el precio y actualizar
        # los contadores del tipo de comprador y sus ingresos.
        # Suma el costo del boleto a los ingresos totales.
        if comprador == 1: 
            total_estudiantes += 1
            ingresos_estudiantes += PRECIO_ESTUDIANTE
            ingresos_totales += PRECIO_ESTUDIANTE
        elif comprador == 2: 
            total_adulto += 1
            ingresos_adultos += PRECIO_ADULTO
            ingresos_totales += PRECIO_ADULTO
        elif comprador == 3: 
            total_tercera_edad += 1
            ingresos_tercera_edad += PRECIO_TERCERA_EDAD
            ingresos_totales += PRECIO_TERCERA_EDAD
        else: 
            total_academico += 1
            ingresos_academicos += PRECIO_ACADEMICO
            ingresos_totales += PRECIO_ACADEMICO
        

    else:
        # Si la edad no es permitida, muestra un mensaje y actualiza el contador ()
        print("ACCESO DENEGADO: El comprador es menor de 13 años.")
        total_rechazados += 1  # Contador de personas rechazadas

    # Pregunta al usuario si desea registrar otra venta.
    continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower()

# --- FIN DEL CICLO ---

# --- 5. Cálculo de Promedio ---
# Calcula el promedio de edad. Cuidado con la división entre cero si no hubo asistentes.
promedio_edad = 0

if total_asistentes > 0:
    promedio_edad = suma_edades / total_asistentes
else: 
    print('No hubo asistentes')

print('^'*50)
print('-'*50)

# --- 6. Impresión del Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")
print(f'Total de Estudiantes: {total_estudiantes}')
print(f'Total de Adultos: {total_adulto}')
print(f'Total de Tercera Edad: {total_tercera_edad}')
print(f'Total de Academicos: {total_academico}')
print('-'*50)

# Imprime todos los totales de asistentes por tipo y sexo.
print("\n--- Estadísticas del Público ---")
print(f'Total de Hombres: {total_hombres}')
print(f'Total de Mujeres: {total_mujeres}')
print('-'*50)
print(f'Total de Asistentes: {total_asistentes}')
print(f'Promedio de edad de asistentes: {promedio_edad:.2f} años')
print(f'Personas rechazadas por edad: {total_rechazados}')


# Imprime todos los ingresos por tipo de comprador y el total general.
# Utiliza formato para mostrar dos decimales en el dinero.
print("\n--- Reporte de Ingresos ---")
print(f'Ingreso por Estudiantes: $ {ingresos_estudiantes:.2f}')
print(f'Ingreso por Adultos: $ {ingresos_adultos:.2f}')
print(f'Ingreso por Tercera Edad: $ {ingresos_tercera_edad:.2f}')
print(f'Ingreso por Academicos: $ {ingresos_academicos:.2f}')
print('-'*50)
print(f'TOTAL RECAUDADO: $ {ingresos_totales:.2f}')
print('-'*50)


# --- 7. Mensaje de Rentabilidad ---
# Usa una estructura if/elif/else para determinar si las ganancias
# fueron BAJAS, MODERADAS o BUENAS, basándote en los ingresos totales.
print("\n--- Rentabilidad ---")

mensaje_rentabilidad = ""
if ingresos_totales < 1500:
    mensaje_rentabilidad = "La función generó BAJAS ganancias."
elif ingresos_totales < 3500:
    mensaje_rentabilidad = "La función generó ganancias MODERADAS."
else: 
    mensaje_rentabilidad = "La función generó BUENAS ganancias."
    
print(mensaje_rentabilidad)


"""
Preguntas: Explica con tus palabras

1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. 
¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

Respuesta:
Crear una variable donde designaremos el día de descuento para almacenar los registros de ventas, después agregamos un if que valide el día de compra, agregamos otro if donde se haga el descuento dependiendo del día (que solo aplicara a martes), por ultimo agregaríamos un if donde marque la edad del comprador, denotando si es adulto o no. Esto se agregaría en el punto 4


2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, 
aunque los ingresos por cada tipo de comprador parecen correctos. 
Describe, paso a paso, qué harías para encontrar el error. 
¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

Respuesta:
Verificaría que en el apartado donde se guardan los ingresos por tipo estén ejecutándose correctamente, para lo cual probaría un tipo de comprador y corroboraría que esta generado correcto, si no funciona agregaría un print donde pondría ingresos totales, para poder corroborar la suma total
"""