# p117-agregar-diccionario.py
# • Crea un diccionario llamado ventas con los siguientes datos: Juan: 1550, Jose: 2600, Maria: 2220.
# • Muestra el diccionario.
# • Agrega los siguientes vendedores y sus ventas al diccionario:
    # o Rocio: 2500 (usando []).
    # o Mateo: 1567 (usando []).
    # o Andrea: 9567 (usando update()).
    # o Miguel: 1234 (usando update()).
# • Muestra el diccionario actualizado.

ventas = {
    'Juan': 1550,
    'Jose': 2600,
    'Maria': 2220
}


print('Ventas Iniciales :')
print(ventas)

ventas['Rocio'] = 2500
ventas['Mateo'] = 1567

ventas.update({'Andrea': 9567, 'Miguel': 1234})

print('Ventas actualizadas :')
print(ventas)