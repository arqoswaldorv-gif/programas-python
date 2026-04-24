# p131-func-mas-param.py
# Funcion con n prametros

def saluda_todos(*todos:str) -> None:
    for nombre in todos:
        print(f'Saludos a {nombre}')
    print()


print('\033[H\033[J')
saluda_todos('Erik')
saluda_todos('Erik','Karina')
saluda_todos('Erik','Karina','Carlos')