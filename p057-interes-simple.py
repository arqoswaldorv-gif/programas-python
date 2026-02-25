# p057-interes-simple.py
# Calcular lso años necesarios para alcanzar una meta de ahorro con un interes simple

while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Calculadora de años para meta de ahorro con interés simple')
    print('-'*60)
    
    capital_inicial = float(input('Capital Inicial : '))
    tasa_interes = float(input('Tasa de interes anual (%) : '))
    meta_ahorro = float(input('Meta de ahorro : '))
    
    capital_actual = capital_inicial
    años = 0
    interes_anula_fijo = capital_inicial  * (tasa_interes/100)
    
    while capital_actual <= meta_ahorro:
        capital_actual += interes_anula_fijo
        años += 1
        
    print('-'*60)
    print(f'Para alcanzar $ {meta_ahorro}, necesitas {años} años')
    print(f'El monto final sera de $ {capital_actual}')
        
    
    if input('\n¿Deseas continuar (S/N)? ').upper()=='N': break
    
print('\nProceso terminado')