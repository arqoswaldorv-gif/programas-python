# p028-retira-cuenta.py
# Simula el retiro de dinero de una cuenta de ahorros revisa el saldo

saldo_actual = 15000.00
print('Simulacro de retiro')
print('\033[2J\033[H')
print(f'TU saldo inicial es de {saldo_actual:.2f}')

cantidad_retiro = float(input('Cantidad a retirar : $ '))

if cantidad_retiro > 0:
    if cantidad_retiro <= saldo_actual:
        print('Iniciadno con el retiro ...')
        saldo_actual -= cantidad_retiro
        print('Retiro Exitoso')
        print(f'Tu nuevo slado es : {saldo_actual:.2f}')
    else: 
        print('\n Fondos Insuficientes para completar la transaccion')
else:
    print('\nLa cantidad a retirar debe de ser un numero positivo')

print('\n Proceso terminado')