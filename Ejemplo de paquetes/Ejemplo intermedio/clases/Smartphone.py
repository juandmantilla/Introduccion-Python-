
from clases.Celular import * 
class Smartphone(Celular):

    def __init__(self, marca, modelo, color, numeroCelular, apps):
        super().__init__(marca, modelo, color, numeroCelular)
        self.apps = apps

    def marcar(self, numero):
        print("Llamando desde smartphone al número " + str(numero))

    
    def recibir (self, numero):
        print("Recibiendo llamada desde smartphone del número" + str(numero))

    def iniciarApps(self, appIniciar):
        print("Ejecutando ... " + str(appIniciar))

    