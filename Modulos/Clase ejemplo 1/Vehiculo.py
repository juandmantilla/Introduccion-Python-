class Vehiculo():

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo    
        self.color = color
        
    def costoVehiculo(self, tasaInflacion, costoVehiculo):
        if(tasaInflacion >= 0.03):
            r = costoVehiculo*tasaInflacion
        else:
            r = costoVehiculo*tasaInflacion + 0.05
        
        return r
