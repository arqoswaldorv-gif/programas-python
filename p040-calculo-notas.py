# p040-calculo-notas.py
# Problema: Escribe un programa que calcule el promedio de 5 calificaciones ingresadas por el usuario. Basado en el promedio, el programa deberá mostrar uno de los siguientes mensajes:
# • Menor a 6: "Quedas reprobado"
# • Desde 6 hasta menos de 7: "Pasas de panzazo"
# • Desde 7 hasta menos de 8: "Muy bien, puedes mejorar"
# • Desde 8 hasta menos de 9: "Excelente, sigue así"
# • Desde 9 hasta 10: "Perfecto, tu esfuerzo valió la pena"
# Ejemplo de ejecución:
# • Entrada: 10, 9, 8, 7, 6
#• Salida: Tu promedio es 8.0. Excelente, sigue así. 

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('--- Verificar notas ---')

print('Ingresa tus calificaciones por espacios:')
cal1, cal2, cal3, cal4, cal5 = input().split()
cal1, cal2, cal3, cal4, cal5 = float(cal1), float(cal2), float(cal3), float(cal4), float(cal5)

promedio = (cal1 + cal2 + cal3 + cal4 + cal5) / 5

if promedio < 6:
    print('Quedas reprobado')
elif promedio < 7:
    print('Pasa de panzazo')
elif promedio < 8:
    print('Muy bien, puedes mejorar')
elif promedio < 9:
    print('Excelente, sigue asi')
elif promedio <= 10:
    print('Perfecto, tu esfuerzo valio la pena')
else:
    print('Error: tu promedio es mayor a 10')

print('\nProceso terminado ...')