class cartas():
    def __init__(self, palo, valor):
        self.__palo = palo
        self.__valor = valor
        self.estado = "en mazo"

    def __str__(self):
        return f"{self.__valor} de {self.__palo}"

    
    def cambiarEstado(self, nuevoEstado):
        self.estado = nuevoEstado
    
    def barajar(self):
        import random
        self.estado = "barajada"
        return random.shuffle(self)

class baraja():
    def __init__(self):
        self.cartas = []
        palos = ["Espadas", "Bastos", "Oros", "Copas"]
        valores = ["As", "2", "3", "4", "5", "6", "7",  "10", "Caballo", "Rey"]
        for palo in palos:
            for valor in valores:
                self.cartas.append(cartas(palo, valor))
    
    def __str__(self):
        return f"Baraja de {len(self.cartas)} cartas"
    
    def barajar(self):
        import random
        random.shuffle(self.cartas)
        for carta in self.cartas:
            carta.cambiarEstado("barajada")

class jugadorDeTruco():
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
    
    def __str__(self):
        return f"Jugador {self.nombre} con {len(self.mano)} cartas en mano"
    
    def robarCarta(self, baraja):
        if len(baraja.cartas) > 0:
            cartaRobada = baraja.cartas.pop()
            cartaRobada.cambiarEstado("en mano")
            self.mano.append(cartaRobada)
            return cartaRobada
        else:
            print("No hay más cartas en la baraja")
            return None
        
def partida():
    barajaJuego = baraja()
    barajaJuego.barajar()

    #Creación de jugadores preguntando por consola los nombres
    jugador1 = jugadorDeTruco(input("Introduce el nombre del jugador 1: "))
    jugador2 = jugadorDeTruco(input("Introduce el nombre del jugador 2: "))

    #jugador1 = jugadorDeTruco("Juan")
    #jugador2 = jugadorDeTruco("Pedro")
    
    for _ in range(3):
        jugador1.robarCarta(barajaJuego)
        jugador2.robarCarta(barajaJuego)
    
    print(jugador1)
    for carta in jugador1.mano:
        print(carta)
    
    print(jugador2)
    for carta in jugador2.mano:
        print(carta)
        
        
def jugarEnvido():
    print("Función para jugar Envido (pendiente de implementación)")
    
def jugarTruco():
    print("Función para jugar Truco (pendiente de implementación)")

#inicio del juego
partida()


