# p120-contar-caracteres.py
# Escribe un programa que pida al usuario que ingrese una cadena de texto.
# • Crea un diccionario vacío para almacenar la frecuencia (cantidad de apariciones) de cada carácter.
# • Itera sobre cada carácter en la cadena ingresada.
# • En cada iteración:
    # o Si el carácter no existe como llave en el diccionario, agrégalo con un valor de 1.
    # o Si el carácter ya existe, incrementa su valor actual en 1.
# • Al finalizar el ciclo, muestra el diccionario resultante con el conteo de caracteres.

resultado = {}

print('\033[H\033[J')
cadena = input('Ingresa una cadena: ')

for letra in cadena:
    if letra not in resultado:
        resultado.update({letra: 1})
    else:
        resultado.update({letra: resultado.get(letra) + 1})

print('Resultado: ')
print(resultado)