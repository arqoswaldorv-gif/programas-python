# p091-iterar-lista.py
# Mostrar las diferentes formas de iterar (pasar) por cada elemeto de la lista

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Iterar los elemetnso a una lista')

nums = [2,4,6,8,10,12,14,16]

print(f'Todos los numeros: {nums} - {len(nums)}')

print('1.-Iteracion por elemento')
for n in nums:
    print(n, end=' ')

print('2.-Iteracion por indice de cada elemetno')    
for i in range(len(nums)):
    print(nums[i], end=' ')
    
print('\n\n3.-Iterar por cada elemento y sumar 2')
for n in nums:
    print(n+2, end=' ')
    
print('\n\n4.-Iterar por indice y sumar 10')
for i in range(len(nums)):
    print(nums[i]+10, end=' ')
    
    
print('5.-Iteracion con enumerate()')
print('Pos\tValor')
for i, n in enumerate(nums):
    print(i, '\t', n)
    
print(f'\n\nResultado: {nums} - {len(nums)}')

print(f'Modificar la lista al iterar')
for i in range(len(nums)):
    nums[i] = nums[i] ** 2

print(f'\n\nResultado: {nums} - {len(nums)}')