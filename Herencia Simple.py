class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("Hola estoy hablando un poco..")

class Empleado(Persona):# Hereda de la clase Persona
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad) # Se agrega los atributos de la Clase padre
        self.trabajo=trabajo
        self.salario=salario # Se agrega los demas atributos para la clase Hija

    def hablar(self):
        print("NO")

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, grado, escuela):
        super().__init__(nombre, edad, nacionalidad)
        self.grado = grado
        self.escuela = escuela

    def saludo(self):
        print(f"Hola soy {self.nombre}, estoy en {self.grado} en el colegio {self.escuela}")

class Jefe(Persona):
    def __init__(self, nombre, edad, nacionalidad, empresa, ingresos, experiencia):
        super().__init__(nombre, edad, nacionalidad)
        self.empresa=empresa
        self.ingresos=ingresos 
        self.experiencia=experiencia

    def saludo(self):
        print(f"Hola soy {self.nombre} soy el jefe de la empresa {self.empresa}, y tengo {self.experiencia} de años en la industria")

persona=Persona("Roberto", 43, "ecuatoriano")
print(persona.nombre, persona.nacionalidad)

empleado=Empleado("Camilo", 20, "Ruso", "primeros auxilios", "2000")
print(empleado.nombre + ",", empleado.trabajo)

estudiante=Estudiante("Vanessa", 17, "Lojana", "Tercero de Bachillerato", "San Francisco de Asís")
estudiante.saludo()

jefe=Jefe("Kelvi", 45, "Estadounidense", "ABACOM", "60000", 23)
jefe.saludo()