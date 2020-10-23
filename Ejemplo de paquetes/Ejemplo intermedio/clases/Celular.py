from clases.Telefono import *

class Celular(Telefono):


    def __init__(self, marca, modelo, color, numeroCelular):
        super().__init__(marca, modelo, color)
        self.numeroCelular = numeroCelular


    def marcar(self, numero):
        print("Llamando desde celular al número " + str(numero))

    
    def recibir (self, numero):
        print("Recibiendo llamada desde celular del número" + str(numero))

    def enviarSMS(self, numero, mensaje):
        print("Mensaje : " + str(mensaje) + " al número " + str(numero))

    
