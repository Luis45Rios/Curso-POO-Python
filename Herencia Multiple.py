class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("Hola estoy hablando un poco..")

class Artista:
    def __init__(self, hablilidad):
        self.habilidad=hablilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")

class EstdianteArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario=salario 
        self.empresa=empresa
    
    def mostrar_habilidad(self):
        print("No tengo habilidad")

    def presentarse(self):
        return f"{super().mostrar_habilidad()}"

estudianteArtista=EstdianteArtista("Luis", 25, "ecuatoriano", "Cantar", 200, "GranMaster Producciones")

estudianteArtista.presentarse()