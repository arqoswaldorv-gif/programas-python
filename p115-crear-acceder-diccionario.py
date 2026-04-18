# p115-crear-acceder-diccionario.py
# • Crea un diccionario llamado dias usando llaves numéricas para los días de la semana.
# • Muestra el diccionario completo.
# • Accede y muestra los siguientes valores específicos:
    # o El valor de la llave 1 (usando []).
    # o El valor de la llave 7 (usando []).
    # o El valor de la llave 5 (usando get()).
    # o El valor de la llave 7 (usando get()).
# • Vuelve a mostrar el diccionario completo.

dias = {
    1: 'Lunes',
    2: 'Martes',
    3: 'Miercoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sabado',
    7: 'Domingo'
}

valor_especifico1 = [1,7]
valor_especifico2 = [5,7]

print('\033[H\033[J')
print('Lista de dias\n')

print(f'Dias de la semana : {dias}')

print('Accedeindo a elemetnos: ')
for v in valor_especifico1:
    print(f'Llave {v} (con []): {dias[v]}')
    
for v in valor_especifico2:
    print(f'Llave {v} (con get()): {dias.get(v)}')

print(f'Dias de la semana : {dias}')