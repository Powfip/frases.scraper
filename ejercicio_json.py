import json

class Vehiculo:
    def __init__(self, tipo_vehiculo, fabricante, modelo, año, color, kilometros, combustible):
        self.tipo_vehiculo = tipo_vehiculo
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.color = color
        self.kilometros = kilometros
        self.combustible = combustible
        
    def to_dict(self):
        return self.__dict__
        
    def mostrar_info(self):
        return (
            f"Tipo de vehículo: {self.tipo_vehiculo}\n"
            f"Fabricante: {self.fabricante}\n"
            f"Modelo: {self.modelo}\n"
            f"Año: {self.año}\n"
            f"Color: {self.color}\n"
            f"Kilometros: {self.kilometros}\n"
            f"Combustible: {self.combustible}"
        )
        
        
class Coche(Vehiculo):
    def __init__(self, tipo_vehiculo, fabricante, modelo, año, color, kilometros, combustible, puertas, cambio, tipo_coche):
        super().__init__(tipo_vehiculo, fabricante, modelo, año, color, kilometros, combustible)
        self.puertas = puertas
        self.cambio = cambio
        self.tipo_coche = tipo_coche
        
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "puertas": self.puertas,
            "cambio": self.cambio,
            "tipo_coche": self.tipo_coche
        })
        return data
        
    def mostrar_info(self):
        base_info = super().mostrar_info()
        return (
            base_info + "\n"
            f"Puertas: {self.puertas}\n"
            f"Cambio: {self.cambio}\n"
            f"Tipo de coche: {self.tipo_coche}"
        )
        
class Moto(Vehiculo):
    def __init__(self, tipo_vehiculo, fabricante, modelo, año, color, kilometros, combustible, cilindradas, tipo_moto):
        super().__init__(tipo_vehiculo, fabricante, modelo, año, color, kilometros, combustible)
        self.cilindradas = cilindradas
        self.tipo_moto = tipo_moto
        
    def to_dict(self):
        data =  super().to_dict()
        data.update({
            "cilindradas": self.cilindradas,
            "tipo_moto": self.tipo_moto
        })
        return data
        
    def mostrar_info(self):
        base_info = super().mostrar_info()
        return (
            base_info + "\n"
            f"Cilindradas: {self.cilindradas}\n"
            f"Tipo de moto: {self.tipo_moto}"
        )
        
class Camion(Vehiculo):
    def __init__(self, tipo_vehiculo, fabricante, modelo, año, color, kilometros, combustible, cambio, ejes):
        super().__init__(tipo_vehiculo, fabricante, modelo, año, color, kilometros, combustible)
        self.cambio = cambio 
        self.ejes = ejes
        
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "cambio": self.cambio,
            "ejes": self.ejes
        })
        return data
        
    def mostrar_info(self):
        base_info = super().mostrar_info()
        return (
            base_info + "\n"
            f"Cambio: {self.cambio}\n"
            f"Ejes: {self.ejes}"
        )
        
def crear_vehiculo():
    tipos_validos = ["Coche", "Moto", "Camion"]
    cambios_validos = ["Automatico", "Manual"]
    combustible_validos = ["Gasolina", "Diesel", "Hibrido"]
    
    while True:
        tipo_vehiculo = input("¿Es un Coche, Moto y Camion? ").strip().capitalize()
        if tipo_vehiculo in tipos_validos:
            break
        print("Tipo de vehículo no válido. Debe ser Coche, Moto o Camion.")
    
    fabricante = input("¿Fabricante? ").strip().capitalize()
    modelo = input("¿Modelo? ").strip().capitalize()
    
    while True:
        try:
            año = int(input("¿Año? "))
            break
        except ValueError:
            print("Año no válido. Debe ser en númmero.")
            
    color = input("¿Color? ").strip().capitalize()
    
    while True:
        try:
            kilometros = float(input("¿Cuántos kilometros? "))
            break
        except ValueError:
            print("Tipo de kilometraje no válido. Debe ser en número.")
            
    while True:
        combustible = input("¿Gasolina / Diesel / Hibrido? ").strip().capitalize()
        if combustible in combustible_validos:
            break
        print("Tipo de combustible no válido. Debe ser Gasolina, Diesel, Hibrido.")
        
    if tipo_vehiculo == "Coche":
        while True:
            try:
                puertas = int(input("¿Cuántas Puertas? "))
                break
            except ValueError:
                print("Tipo de puertas no válido. Debe ser en número.")
                
        while True:
            cambio = input("¿Automatico / Manual? ").strip().capitalize()
            if cambio in cambios_validos:
                break
            print("Tipo de cambio no válido. Debe ser Automatico o Manual.")
            
        tipo_coche = input("¿Es Turismo / Suv / Todo Terreno? ").strip().capitalize()
        return Coche(tipo_vehiculo, fabricante, modelo, año, color, kilometros, combustible, puertas, cambio, tipo_coche)
    
    elif tipo_vehiculo == "Moto":
        while True:
            try:
                cilindradas = int(input("¿Cilindradas? "))
                break
            except ValueError:
                print("Tipo de cilindradas no válido. Debe ser en número.")
                
        tipo_moto = input("¿Deportiva / Scooter? ").strip().capitalize()
        return Moto(tipo_vehiculo, fabricante, modelo, año, color, kilometros, combustible, cilindradas, tipo_moto)
    
    elif tipo_vehiculo == "Camion":
        while True:
            cambio = input("¿Automatico / Manual? ").strip().capitalize()
            if cambio in cambios_validos:
                break
            print("Tipo de cambio no válido. Debe ser Automatico o Manual.")
            
        while True:
            try:
                ejes = int(input("¿Número de ejes? "))
                break
            except ValueError:
                print("Número de ejes inválido.")
        return Camion(tipo_vehiculo, fabricante, modelo, año, color, kilometros, combustible, cambio, ejes)
        
vehiculo = crear_vehiculo()

with open("vehiculo.json", "w") as archivo:
    json.dump(vehiculo.to_dict(), archivo, indent=4)
print("Vehiculo guardada en 'vehiculo.json'.")

with open("vehiculo.json", "r") as archivo:
    vehiculo_cargado = json.load(archivo)
print("Vehiculo cargado desde 'vehiculo.json'.")
for clave, valor in vehiculo_cargado.items():
    print(f"{clave.capitalize()}: {valor}")

