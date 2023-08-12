class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")

estudiante1= Estudiante(input("Por favot ingrese su nombre: "), int(input("Por favor ingresa tu edad: ")), input("Por favor ingresa tu grado: "))

estudiar=input()
if estudiar.lower() == "estudiar":
    estudiante1.estudiar()
else:
    pass