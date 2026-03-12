# p087-acceder-lista.py
# Acceder a los elementos de una lista por su indice

nums = [10,20,30,40,60,70,10,20,99]

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

print('Acceder a los elementos de una lista')


print('\nLongitud y contenido')
print(f'CUantas mediciones son : {len(nums)}')
print(f'Todas las mediciones : {nums}')

print('\nPrimera y Ultima medicion, por indice Positivo')
print(f'La Primera : {nums[0]}')
print(f'La Ultima : {nums[8]}')

print('\nPrimera y Ultima medicion, por indice Negativo')
print(f'La Primera : {nums[-9]}')
print(f'La Ultima : {nums[-1]}')

print('\nPor Rango : ')
print(f'Las mediciones de la 2 a la 6 (sin incluir la 6) : {nums[2:6]}')

print('\nPor Saltos consecutivos')
print(f'Las primeras 3 mediciones, inicando de la izqueirda : {nums[:3]}')
print(f'Las ultimas 3 mediciones, desde la 6 hasta el final : {nums[6:]}')