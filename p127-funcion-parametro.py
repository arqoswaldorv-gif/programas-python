# p127-funcion-parametro.py
print('\033[H\033[J')

# Declaracion
def saluda(nombre) -> None:
    print(f'Hola {nombre} bienveniod a Python, tu nombre tiene {len(nombre)} caracteres')
    print()

# llamado
saluda('Gustavo Daniel')
saluda('Juan Perez Diaz')
saluda('Maria Soto Garcia')