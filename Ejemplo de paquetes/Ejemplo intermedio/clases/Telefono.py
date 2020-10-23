class Telefono():

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo 
        self.color = color 

    
    def marcar(self, numero):
        print("Llamando al número" + str(numero))

    def recibir(self, numero):
        print("Recibiendo número de " + str(numero))

    
