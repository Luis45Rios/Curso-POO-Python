class Alumno:
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self.nota >= other
    def aprobado(self):
        print(f"El estudiante {self.nombre} tiene {self.nota} y esta aprobado")

    def reprobado(self):
        print(f"El estudiante {self.nombre} tiene {self.nota} y esta reprobado")

nombre=input("Nombre del estudiante")
nota=input("Por favor imgrese la nota del estudiante")

estudiante1=Alumno(nombre, float(nota))

if estudiante1 >= 7.0:
    estudiante1.aprobado()
else:
    estudiante1.reprobado()