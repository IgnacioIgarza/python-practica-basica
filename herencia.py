class vehiculos (object):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True
        
    def estado(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, En Marcha: {self.enMarcha}, Acelerando: {self.acelera}, Frenando: {self.frena}"
    

class Furgoneta(vehiculos):
        def carga(self, cargar):
            self.cargado = cargar
            if self.cargado:
                return "La furgoneta está cargada"
            else:
                return "La furgoneta no está cargada"
            
class Moto(vehiculos):
    hCaballito = "no"
    def caballito(self):
        self.hCaballito = "Voy haciendo el caballito"
    
    def estado(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, En Marcha: {self.enMarcha}, Acelerando: {self.acelera}, Frenando: {self.frena}, Caballito: {self.hCaballito}"

moto1 = Moto("Honda", "CBR")
moto1.arrancar()
moto1.acelerar()
print(moto1.estado())

#herencia multiple
class VElectricos():
    def __init__(self):
        self.autonomia = 100
    
    def cargarEnergia(self):
        self.cargando = True
        
class MotoElectrica(Moto, VElectricos):
    def __init__(self, marca, modelo):
        Moto.__init__(self, marca, modelo)
        VElectricos.__init__(self)
        
motoE1 = MotoElectrica("Yamaha", "MT-07")
motoE1.arrancar()
motoE1.cargarEnergia()
print(motoE1.estado())

