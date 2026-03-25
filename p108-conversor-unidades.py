# p108-conversor-unidades.py
# COnvertir de diferentes unidades de longitud a metros usando diccionarios


print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
print('Convertir de diferentes unidades de longitud a metros usando diccionarios')

conv = {
    'km': 1000,
    'm': 1,
    'cm': 0.01,
    'mm': 0.001,
}

while True:
    try:
        long = int(input('Dame la longitud en metros : '))
        break
    except ValueError:
        continue

while True:
    uni = input('A que Unidad deseas convertir (Km, m, cm, mm): ')
    if uni in conv: break
    else: continue

res = long / conv[uni]
    
# print(f'{long:,.2f} {uni} son {res:,.2f} metros')
print(f'{long:,.4f} metros, equivalen a {res:,.4f} {uni}')