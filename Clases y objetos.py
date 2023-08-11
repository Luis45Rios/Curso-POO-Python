class Celular:
    def __init__(self, marca, modelo, camara, color):
        self.marca=marca
        self.modelo=modelo
        self.camara=camara
        self.color=color

    def llamada_entrante(self):
        print(f"Te estan llamando desde un telefono {celular1.modelo}")

    def cortar_llamada(self):
        print(f"La llamada se ha cancelado desde un telefono {celular2.modelo}")

    # Atributos Estaticos
    #marca = "Xiaomi"
    #camara = "48MP"

# Instanciar la clase
celular1 = Celular("Xiaomi", "Redmi 9T", "50MP", "Gris")
celular2 = Celular("Apple", "IPhone 13 Pro", "60MP", "Cyan")
print(celular1.color)
print(celular2.color)

celular1.llamada_entrante()
celular2.cortar_llamada()

# Son modiificables a fuera de la clase
#celular1.camara="50MP"     "Consola: 50MP"