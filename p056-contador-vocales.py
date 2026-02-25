# p056-contador-vocales.py
# Cuenta vocales, consonantes y otros caracteres en una frase

while True:
    print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla
    print('Contador de vocales y consonantes')
    frase = input('Introduce una frase : ')
    
    vocales = consonantes = otros = 0
    indice = 0
    
    while indice < len(frase):
        caracter = frase[indice] # Tomamos el caracter correspondiente de la frase
        
        if caracter >= 'a' and caracter <= 'z': # Verificamos que sea letra
            if caracter in 'aeiou':
                vocales += 1
            else: # es consonatnes
                consonantes += 1
        else: # es cualqueir otra cosa
            otros += 1
            
        indice += 1
    
    print(f'Análisis de la frase')
    print(f'Número de vocales     : {vocales}')
    print(f'Número de consonantes : {consonantes}')
    print(f'Número de otros       : {otros}')
    
    if input('\n¿Deseas continuar (S/N)? ').upper()=='N': break
    
print('\nProceso terminado')