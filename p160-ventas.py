# p160-ventas.py
# Simular un sistema de control de ventas

class Venta:
    def __init__(self, articulo, cantidad, precio):
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = precio
        self.total = self.cantidad * self.precio #calculada

    def __str__(self):
        return f'Articulo:{self.articulo:<15} Cantidad:{self.cantidad:>10.2f} Precio:{self.precio:>10.2f} Total:{self.total:>10,.2f}'

class Cliente:
    def __init__(self, rfc, nombre, domicilio, correo):
        self.rfc = rfc
        self.nombre = nombre
        self.domicilio = domicilio
        self.correo = correo
        self.ventas = list()

    def agregarVenta(self, venta):
        self.ventas.append(venta)

    def totalVentas(self):
        total = 0
        for venta in self.ventas:
            total += venta.total
        return total

    def __str__(self):
        return f'Cliente [Nombre: {self.nombre:<20} RFC:{self.rfc:<12} Domicilio: {self.domicilio:<20} Correo: {self.correo:<20}]'

class Tienda:
    def __init__(self, nombre, domicilio, propietario):
        self.nombre = nombre
        self.domicilio = domicilio
        self.propietario = propietario
        self.clientes = list()

    def agregarCliente(self, cliente):
        self.clientes.append(cliente)

    def totalGeneral(self):
        total = 0
        for cliente in self.clientes:
            total += cliente.totalVentas()
        return total

    def __str__(self):
        return f'Tienda [Nombre:{self.nombre} Domicilio:{self.domicilio} Prietario:{self.propietario}]'

def main():
    # Todo
    print('\033[H\033[J')
    mitienda = Tienda(nombre='Ferrateria las Lomas', domicilio='Av Luis Moya 345', propietario='Carlos Castaneda')
    mitienda.agregarCliente( Cliente(rfc='JELI120240', nombre='Felipe Calderon', domicilio='Las Lomas 123', correo='calde@msn.com') )
    mitienda.agregarCliente( Cliente(rfc='PEÑA121250', nombre='Enrique Peña', domicilio='5 de Mayo 321', correo='quique@gmail.com') )
    mitienda.agregarCliente( Cliente(rfc='AMLO101145', nombre='Andres Lopez', domicilio='Palacio Nacional 321', correo='peje@yahoo.com') )
    mitienda.agregarCliente( Cliente(rfc='GELA666666', nombre='Xochitl Gelatinas', domicilio='Danone 123', correo='xochitl@precidencia.gob.mx') )
    mitienda.clientes[0].agregarVenta( Venta(articulo='Martillo', cantidad=10, precio=60.5) )
    mitienda.clientes[0].agregarVenta( Venta(articulo='Pala', cantidad=2, precio=1170.55) )
    mitienda.clientes[1].agregarVenta( Venta(articulo='Clavo', cantidad=2.5, precio=160.34) )
    mitienda.clientes[1].agregarVenta( Venta(articulo='Cinta de Aislar', cantidad=5, precio=71.34) )
    mitienda.clientes[1].agregarVenta( Venta(articulo='Pinzas', cantidad=10, precio=650.33) )
    mitienda.clientes[2].agregarVenta( Venta(articulo='Thiner', cantidad=50, precio=65.00) )

    print(f'\nReporte de Ventas: {mitienda}\n')
    print('\nClientes:')
    for cliente in mitienda.clientes:
        print(cliente)

    print('\nVentas de cada cliente')
    for cliente in mitienda.clientes:
        print(f'\n{cliente.rfc} - {cliente.nombre} - {cliente.totalVentas():,.2f}')
        for venta in cliente.ventas:
            print(f'{venta}')

    print(f'\nTotal de Ventas Genera: {mitienda.totalGeneral():,.2f}')

""" # Programa principal
print('\033[H\033[J')
v1 = Venta('Martillo', 10, 100)
v2 = Venta('Pala', 5, 300)
v3 = Venta('Cinta de Medir', 2, 400)

c1 = Cliente('carc711202pc9', 'Carlos', 'Av Mexico 113', 'castr@hotmail.com')
c1.agregarVenta(v1)
c1.agregarVenta(v2)
c1.agregarVenta(v3)
print(c1)
print(c1.ventas[0])
print(c1.ventas[1])
print(c1.ventas[2])
print(c1.totalVentas())
"""

if __name__ == '__main__':
    main()