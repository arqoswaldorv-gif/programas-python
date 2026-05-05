# p157-empleado2.py
# Modelamos un empleado usando una clase, agregamos mas atributos

# Codigo de Clase
class Empleado:
    def __init__(self, nombre, edad, sexo, casado):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.casado = casado
    def __str__(self):
        return f"Nombre:{self.nombre}, Edad: {self.edad}, Sexo: {"Mujer" if self.sexo== "M" else "Hombre"}, Casado: {"Casad@" if self.casado else "solter@"} \n"
    


    # Programa principal

    # Instanciamos la clase


empleado1 = Empleado("juan Diaz", 35, "H", True)
print("\033[H\033[J")
print(f"Nombre      : {empleado1.nombre}")
print(f"Edad        : {empleado1.edad}")
print(f"Sexo        : {empleado1.sexo}")
print(f"Casado      : {empleado1.casado}")
print(empleado1)

empleado2 = Empleado("Rocio Soto", 45, "M", False)
print(f"Nombre      : {empleado2.nombre}")
print(f"Edad        : {empleado2.edad}")
print(f"Sexo        : {empleado2.sexo}")
print(f"Casado      : {empleado2.casado}")
print(empleado2)

empleado3 = Empleado("Pedro Torres", 45, "H", False)
print(f"Nombre      : {empleado3.nombre}")
print(f"Edad        : {empleado3.edad}")
print(f"Sexo        : {empleado3.sexo}")
print(f"Casado      : {empleado3.casado}")
print(empleado3)

suma_edades = empleado1.edad +empleado2.edad + empleado3.edad
promedio_edades = suma_edades /3
print(f"\nPromedio de las edades es : {promedio_edades:.2f}")