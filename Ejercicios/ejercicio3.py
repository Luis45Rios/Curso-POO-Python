class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def __ge__(self, other):
        if isinstance(other, (int)):
            return self.nombre 

    def mayor_edad(self):
        print(f"{self.nombre} es mayor de edad")

    def menor_edad(self):
        print(f"{self.nombre} es menor de edad")

nombre=input("Por favor ingresa tu nombre: ")
edad=int(input("Por favor ingresa tu edad: "))

persona1=Persona(nombre, edad)

if edad >= 18:
    persona1.mayor_edad()
else:
    persona1.menor_edad()