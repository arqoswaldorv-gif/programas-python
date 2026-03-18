# p096-registro-estudiantes.py
# Registro y analisis de asistentes a un evento

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Sistema de Registro para Eventos')

print('Introduce los nombres y edades de los asistentes (* para terminar)')

nombres = []
edades = []

while True:
    nombre = input('Nombre del asistente :')
    if nombre == '*' : break
    try: 
        edad = int(input('Edad : '))
        nombres.append(nombre)
        edades.append(edad)
    
    except ValueError:
        print('Valor erroneo')

if not nombres:
    print('No hay datos para procesar')
else:
    print('Asostentes mayores de Edad')
    encontrados = False
    for i in range(len(nombres)):
        if edades[i] >= 18:
            print(f'Nombre : {nombres[i]} , Edad: {edades[i]}')
            encontrados = True
    if not encontrados:
        print('No hay mayores de edad')

edad_maxima = max(edades)
pos_max = edades.index(edad_maxima)
nombre_max = nombres.index(pos_max)

print(f'\nEl reconocimeto a la persona de mayor edad es para ')
print(f'Nombre: {nombre_max} con edad {edad_maxima} años')