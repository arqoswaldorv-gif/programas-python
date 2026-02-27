# p062-conversion-temperaturas.py
# El usuario debe introducir una temperatura inicial y una final en grados Celsius. El programa mostrará la conversión a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.
# Ejemplo de ejecución:
#   Introduce la temperatura inicial en °C: 5
#   Introduce la temperatura final en °C: 8
#   --------------------
#   5°C = 41.0°F
#   6°C = 42.8°F
#   7°C = 44.6°F
#   8°C = 46.4°F
#   ¿Desea continuar (S/N)? N

while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Temperaturas en Celsius y Fahrenheit')
    print('-'*60)
    
    inicio = int(input('Introduce la temepratura inicial en °C: '))
    final = int(input('Introduce la temepratura final en °C: '))
   
    while True:
        if inicio > final: break
        f = (inicio * 9 / 5) + 32
        print(f'{inicio} °C =  {f} °F')
        inicio += 1
        
  
    
    if input('\n¿Deseas continuar (S/N)? ').upper()=='N': break
    
print('\nProceso terminado')