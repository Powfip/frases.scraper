import pickle

class Animal:
    def __init__(self, tipo, modelo, nombre):
        self.tipo = tipo
        self.modelo = modelo
        self.nombre = nombre
        self.ruido = False
        self.acelera = False
        self.frena = False
        
    def ruido(self):
        self.ruido = True
        
    def correr(self):
        self.acelera = True
        
    def parar(self):
        self.frena = True
        
    def estado(self):
        print(f"Raza {self.tipo},\nColor: {self.color},\nRuido: {self.ruido},\nAcelerando: {self.acelera},\nFrenando: {self.frena}")
animal1 = Animal("Gato", "Gris", "Quasi")
animal2 = Animal("Pez", "Marron", "Rabbit")
animal3 = Animal("Perro", "Rojo", "Pluto")

animales = [animal1, animal2, animal3]
fichero = open("animal.txt", "wb")

pickle.dump(animales, fichero)
fichero.close()

