#herencia multiple con super()
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"    

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Salario: {self.salario}"
    
Juan = Empleado("Juan", 30, 50000)
print(Juan.mostrar_info())

def preguntar_ingresar_empleado():
    respuesta = ""
    while respuesta != "no":
        print("Quiere ingresar un empleado? (si/no)")
        respuesta = input().lower()
        if respuesta == "si":
            ingresar_empleado_e_agregarlo_a_lista()
        elif respuesta == "no":
            print("Gracias por usar el programa.")
        else:
            print("Respuesta no válida. Por favor, ingrese 'si' o 'no'.")

empleados = []
def ingresar_empleado_e_agregarlo_a_lista():
    
    try:
        nombre = input("Ingrese el nombre del empleado: ")
    except ValueError:
        print("Error: El nombre debe ser una cadena de texto.")
        return
    try:
        edad = int(input("Ingrese la edad del empleado: ")) 
    except ValueError:
        print("Error: La edad debe ser un número entero.")
        return
    try:
        salario = float(input("Ingrese el salario del empleado: "))
    except ValueError:
        print("Error: El salario debe ser un número.")
        return
    empleado = Empleado(nombre, edad, salario)
    empleados.append(empleado)
    return empleados

def mostrar_empleados(empleados):
    print("\n**Lista de empleados:**")
    if not empleados:
        print("No hay empleados para mostrar.")
        return
    for empleado in empleados:
        print(empleado.mostrar_info())

preguntar_ingresar_empleado()
mostrar_empleados(empleados)