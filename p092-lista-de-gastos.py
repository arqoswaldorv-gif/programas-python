# p092-lista-de-gastos.py
# Permite llevar el control de una lsita de gasto

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Iterar los elemetnso a una lista')

gastos = [450.50, 120.00, 85.90, 230.00, 55.75]
limite_gasto = 100.00

while True:
    print('\n---Menú de Gestión de Gastos ---')
    print("1.-Ver todos los gastos")
    print("2.-Agrear un nuevo gasto")
    print("3.-Modificar un gasto existente")
    print("4.-Eliminar un gasto (por reembolso o error)")
    print("5.-Ver Resumen y total de gastos")
    print("6.- Salir")
    opcion = int(input('Elige una opcion (1-6) : '))
    
    if opcion ==  1:
        print("\n--- Tus Gastos Registrados ---")
        print(gastos)
    elif opcion == 2:
        try:
            nuevo_gasto = float(input("Ingresa el monto del nuevo gasto: "))
            gastos.append(nuevo_gasto)
            print(f'Gasto de ${nuevo_gasto:.2f} agregado correctamente.')
        except ValueError: 
            print("Error: Por favor, ingresa un número válido.")
    elif opcion == 3:
        try:
            pos = int(input("Ingresa la posición en la lista del gasto que queires modificar: "))
            valor_anterior = gastos[pos]
            print(f'Gasto a modificar gasto[{pos}] ${valor_anterior:.2f}')
            nuevo_valor = float(input("ingresa el nuevo motno del gasto: "))
            gastos[pos] = nuevo_valor
            print(f'Gasto modificado de ${valor_anterior:.2f} a ${nuevo_valor:.2f}.')
        except IndexError: 
            print("Error: La posición especifica no se encuentra en la lista.")
        except ValueError: 
            print("Error: Por favor, ingresa un número válido.")
            
    elif opcion == 4:
        try:
           gasto_a_elimintar = float(input("Ingresa el monto del gasto qeu queires eliminar: "))
           if gasto_a_elimintar in gastos:
               gastos.remove(gasto_a_elimintar)
               print(f'Gasto de ${gasto_a_elimintar:.2f} eliminado correctamente.')
           else:
               print("Error: EL gasto especificado no se encuentra en la lista.")
        except ValueError: 
            print("Error: Por favor, ingresa un número válido.")
            
    elif opcion == 5:
        if not gastos:
            print("\nNo hay gastos para msotrar.")
        else: 
            total_gastado = 0
            print("\n--- Resumen del MEs ---")
            for gasto in gastos:
                total_gastado += gasto
                if gasto > limite_gasto:
                    print(f'Gasto considerable detectado: ${gasto:.2f}')
            print(f'\nEl gasto total del mes es: ${total_gastado:.2f}')
    elif opcion == 6:
        print("\nGracias por usar el gestor de gastos/ ¡Hasta pronto!"); break
    else:
        print("Opcion no válida. Por favor, elige un número del 1 al 6.")