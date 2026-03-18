# p095-precio-acciones.py
# Analisis basico de portafolio de acciones
# max, index

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Encontrar las accioens mas alta y mas baja en una semana')

dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
precios = [150.25, 152.50, 149.75, 155.00, 153.20, 100.00]

precio_max = max(precios)
precio_min = min(precios)

pos_max = precios.index(precio_max)
pos_min = precios.index(precio_min)

print(f'Precios de las accioens en la semana {precios}')
print(f'Dias : {dias}')
print(f'El precio mas alto fue ${precio_max} el dia {dias[pos_max]}')
print(f'El precio mas bajo fue ${precio_min} el dia {dias[pos_min]}')