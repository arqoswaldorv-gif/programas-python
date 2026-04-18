# p116-modificar-diccionario.py
# • Crea un diccionario llamado paises con los siguientes pares (llave: valor): Argentina: 100, Brasil: 200, Colombia: 300, Chile: 400, Ecuador: 500, Bolivia: 600, Jamaica: 700.
# • Muestra el diccionario inicial.
# • Modifica los valores de las siguientes llaves:
# o Cambia el valor de Brasil a 250 (usando []).
# o Cambia el valor de Chile a 450 (usando []).
# o Cambia el valor de Bolivia a 650 (usando update()).
# o Cambia el valor de Jamaica a 750 (usando update()).
# • Muestra el diccionario modificado.

paises = {
    'Argentina': 100,
    'Brasil': 200,
    'Colombia': 300,
    'Chile': 400,
    'Ecuador': 500,
    'Bolivia': 600,
    'Jamaica' : 700
}


print('\033[H\033[J')
print('Lista de paises\n')

print('Diccionario Inicial :')
print(paises)


paises['Brasil'] = 250
paises['Chile'] = 450

paises.update({'Bolivia': 650, 'Jamaica': 750})

print('Diccionario Modificado :')
print(paises)