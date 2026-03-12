# p089-agregar-lista.py
# Mostrar las diferentes formas para agregar elemetnso a una lsita

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Agregar elemetnos a una lista')

nums = [80.3,12.5,60.2,30.4]

print(f'Temperaturas iniciales: {nums} - {len(nums)}')

print(f'Agregar los valores 90 y 10 al final: ')
nums.append(90)
nums.append(100)
print(f'Resutlado: {nums} - {len(nums)}')

print('Insertar el 80 en la posicion 4: ')
nums.insert(4, 80)
print(f'Resutlado: {nums} - {len(nums)}')

print(f'Extender datos agregando [110,120,130] se agregan al final')
nums.extend([110,120,130])
print(f'Resutlado: {nums} - {len(nums)}')