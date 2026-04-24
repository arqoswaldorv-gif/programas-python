# p129-func-param-nombre.py
# Funcion que es invocada con el nombre de los parametros

print('\033[H\033[J')

# Declaracion
def saluda(apaterno:str, amaterno:str, nombre:str) -> None:
    print(f'Hola {nombre} {apaterno} {amaterno}')
    print()
    
# llamado
saluda('Castaneda','Ramirez','Carlos')
saluda(apaterno='Soto',amaterno='Bernal',nombre='Rocio')
saluda(nombre='Juan', amaterno='Diaz', apaterno='Perez')
saluda('Castaneda', amaterno='Villa', nombre='Juan')