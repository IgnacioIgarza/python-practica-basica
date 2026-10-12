class Choches():
    #Atributos o propiedades de la clase
    largo = 200
    ancho = 100
    ruedas = 4
    enMarcha = False
    
    #Metodos de la clase
    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos
        if self.enMarcha:
            return "El coche esta en marcha"
        else:
            return "El coche esta detenido"

    def detener(self):
        self.enMarcha = False
        
    def estado(self):
        print("El coche tiene ", self.ruedas, " ruedas. Un ancho de ", self.ancho, " y un largo de ", self.largo)
        
    
#Construccion de un objeto de la clase Choches
miCoche = Choches()  #Instanciamos la clase Choches y creamos un objeto llamado miCoche

print("El largo del coche es: ", miCoche.largo)
print("El ancho del coche es: ", miCoche.ancho)
print("El coche tiene: ", miCoche.ruedas, "ruedas")
print(miCoche.arrancar(True)) #Llamamos al metodo arrancar del objeto miCoche

print("El estado del coche 1:") 
miCoche.estado()

miCoche2 = Choches()  #Instanciamos la clase Choches y creamos un objeto llamado miCoche2
print(miCoche2.arrancar(False)) #Llamamos al metodo arrancar del objeto miCoche2
print("El estado del coche 2:")
miCoche2.estado()