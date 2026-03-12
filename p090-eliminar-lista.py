# p090-eliminar-lista.py
# Mostrar las diferentes formas de eliminar elementos de una lista

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Agregar elemetnos a una lista')

nums = [1,3,5,7,9,11,99,15,88,19,100]

print(f'Datos originales con anomalias: {nums} - {len(nums)}')

print('Eliminar el valor 99: ')
nums.remove(99)
print(f'Resutlado: {nums} - {len(nums)}')

print('Eliminar el elelemento en la posicion 8')
num_removido = nums.pop(8)
print(f'Resutlado: {nums} - {len(nums)} - Se removio: {num_removido}')

print('Eliminar el ultimo elemtno: ')
num_removido = nums.pop()
print(f'Resutlado: {nums} - {len(nums)} - Se removio: {num_removido}')

print(f'Eliminar todas las mediciones ')
nums.clear()
print(f'Resutlado: {nums} - {len(nums)}')