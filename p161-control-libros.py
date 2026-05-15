# p161-control-libros.py
# Sistema de control de préstamos de libros

class Prestamo:
    def __init__(self, libro, dias, tarifa_diaria):
        self.libro = libro
        self.dias = dias
        self.tarifa_diaria = tarifa_diaria
        self.total = self.dias * self.tarifa_diaria #calculada

    def __str__(self):
        return f' -> Libro:{self.libro:<30} Dias:{self.dias:>5} Tarifa/Día: ${self.tarifa_diaria:>6.2f} Total: ${self.total:>7.2f}'

class Usuario:
    def __init__(self, id_usuario, nombre, correo, telefono):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.prestamos = list()

    def agregarPrestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def totalTarifas(self):
        total = 0
        for prestamo in self.prestamos:
            total += prestamo.total
        return total

    def __str__(self):
        return f'Usuario -> [Nombre: {self.nombre:<20} ID: {self.id_usuario:<12} Correo: {self.correo:<25} Tel: {self.telefono:<12}]'

class Biblioteca:
    def __init__(self, nombre, domicilio, encargado):
        self.nombre = nombre
        self.domicilio = domicilio
        self.encargado = encargado
        self.usuarios = list()

    def agregarUsuario(self, usuario):
        self.usuarios.append(usuario)

    def totalPrestamos(self):
        total = 0
        for usuario in self.usuarios:
            total += len(usuario.prestamos)
        return total

    def totalImportePrestamos(self):
        total = 0
        for usuario in self.usuarios:
            total += usuario.totalTarifas()
        return total

    def __str__(self):
        return f'Biblioteca -> [Nombre: {self.nombre} Domicilio: {self.domicilio} Encargado: {self.encargado}]'

def main():
    print('\033[H\033[J')
    mibiblioteca = Biblioteca(
        nombre='Biblioteca Mauricio Magdaleno',
        domicilio='Calle Grillo 100, Col. Centro',
        encargado='Dra. Leticia Ramírez'
    )
    mibiblioteca.agregarUsuario( Usuario(id_usuario='USR-2026-X', nombre='Salvador Novo',  correo='snovo@cultura.gob.mx',    telefono='4921112233') )
    mibiblioteca.agregarUsuario( Usuario(id_usuario='USR-2026-Y', nombre='Amparo Dávila',  correo='amparo@unam.mx',          telefono='4922223344') )
    mibiblioteca.agregarUsuario( Usuario(id_usuario='USR-2026-Z', nombre='Juan Rulfo',     correo='jrulfo@literatura.mx',    telefono='4923334455') )
    mibiblioteca.agregarUsuario( Usuario(id_usuario='USR-2026-W', nombre='Elena Garro',    correo='egarro@escritores.org',   telefono='4924445566') )

    mibiblioteca.usuarios[0].agregarPrestamo( Prestamo(libro='Laberinto de la Soledad', dias=6,  tarifa_diaria=11.50) )
    mibiblioteca.usuarios[0].agregarPrestamo( Prestamo(libro='Pedro Páramo',            dias=4,  tarifa_diaria=14.00) )
    mibiblioteca.usuarios[1].agregarPrestamo( Prestamo(libro='Balún Canán',             dias=8,  tarifa_diaria=9.50)  )
    mibiblioteca.usuarios[1].agregarPrestamo( Prestamo(libro='Oficio de Tinieblas',     dias=5,  tarifa_diaria=12.00) )
    mibiblioteca.usuarios[1].agregarPrestamo( Prestamo(libro='Árbol de Literatura',     dias=3,  tarifa_diaria=18.00) )
    mibiblioteca.usuarios[2].agregarPrestamo( Prestamo(libro='El Llano en Llamas',      dias=10, tarifa_diaria=7.50)  )

    sep1 = '=' * 90
    sep2 = '-' * 90

    print(f'\n{sep1}')
    print(f'REPORTE DE CONTROL DE PRÉSTAMOS: {mibiblioteca}')
    print(f'{sep1}')
    print(f'Total de usuarios registrados : {len(mibiblioteca.usuarios)}')
    print(f'Total de préstamos activos    : {mibiblioteca.totalPrestamos()}')
    print(f'{sep2}')

    print('\n--- Catálogo de Usuarios Registrados ---')
    for usuario in mibiblioteca.usuarios:
        print(usuario)

    print('\n--- Detalle de Préstamos por Lector ---')
    for usuario in mibiblioteca.usuarios:
        print(f'\n{usuario.id_usuario} - {usuario.nombre} | Costo Acumulado del Lector: ${usuario.totalTarifas():,.2f}')
        for prestamo in usuario.prestamos:
            print(f'{prestamo}')

    print(f'\n{sep1}')
    print(f'IMPORTACIÓN TOTAL RECAUDADA POR LA BIBLIOTECA: ${mibiblioteca.totalImportePrestamos():,.2f}')
    print(f'{sep1}\n')

if __name__ == '__main__':
    main()