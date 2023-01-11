import pickle

class vehiculo:
    marca = ""
    color = ""

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def getMarca(self):
        return self.marca

    def getColor(self):
        return self.color

f = open('datos.bin', 'rb')
carro = pickle.load(f)
f.close()

print("marca:", carro.getMarca(), "color:", carro.getColor())
