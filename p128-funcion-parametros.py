# p128-funcion-parametros.py
# Funcion que recibe multiples parametros

def saluda(apaterno: str, nombre: str) -> None:
    print(f'Hola {nombre} {apaterno}')


print('\033[H\033[J')
saluda('Rodriguez', 'Oswaldo')
saluda('Rocio', 'Soto')

# saluda('Oswaldo') 
# saluda('Rodriguez','Oswaldo,30)