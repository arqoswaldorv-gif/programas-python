# p075-cifrado-cesar.py
# Cifrado un mensaje usando el cifrado de Cesar

print("\033[H\033[J") # imprime una secuencia ansi que borra la pantalla

while True:

    
    print('CIfrando de un mensaje usando el mensaje de ciifrado de Cesar')
    
    mensaje_original = input('Infresa el mesnaje a cifrar ? ')
    desplazamieto = int(input('Desplazamieto (numero) ? '))
    mensaje_cifrado = ""

    for caracter in mensaje_original:
        if caracter.isalpha():
            codigo_ascii = ord(caracter)
            base = ord('a') if caracter.islower() else ord('A')
            codigo_nuevo = base + (codigo_ascii - base + desplazamieto) % 26
            mensaje_cifrado += chr(codigo_nuevo)
        else:
            mensaje_cifrado += caracter
            
    print(f'Mensaje original : {mensaje_original}')
    print(f'Mensaje cifrado : {mensaje_cifrado}')
            
    
    if input('\n\nDesea continuar (S/N) ? ').upper()=='N' : break

print("\nProceso Terminado")