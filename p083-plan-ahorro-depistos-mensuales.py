# p083-plan-ahorro-depistos-mensuales.py
# El programa simulará un plan de ahorro. Deberá solicitar al usuario un monto inicial, un depósito mensual fijo, una tasa de interés mensual (porcentaje), y el número total de meses del plan. El programa debe mostrar una tabla que detalle, para cada mes, el saldo inicial, el interés ganado en ese mes, y el saldo final. El interés se calcula sobre el saldo inicial antes de sumar el nuevo depósito.

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla


monto_inicial = int(input('Monto inicial: '))
deposito_mensual = int(input('Deposito mensual: '))
tasa_interes = float(input('Tasa de interes mensual (%): '))
numero_meses = int(input('Numero de meses: '))

print(f'Monto inical: {monto_inicial}')
print(f'Deposito mensual: {deposito_mensual}')
print(f'Tasa de interes mensual (%): {tasa_interes}')
print(f'Numero de meses a simular: {numero_meses}')

print('--- Plan de Ahorro Detallado ---')

saldo = monto_inicial

for mes in range(1, numero_meses + 1):
    saldo_inicial = saldo
    interes = saldo_inicial * (tasa_interes / 100)
    saldo_final = saldo_inicial + interes + deposito_mensual
    
    print(f'Mes {mes}: Saldo Inicial: ${saldo_inicial:.2f} | Interés: ${interes:.2f} | Saldo Final: ${saldo_final:.2f}')
    
    saldo = saldo_final


print(f'Al final de {numero_meses} meses, tendras ${saldo:.2f}')