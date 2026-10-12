#para ejecutar por consola: comando py y luego el nombre del archivo, por ejemplo: py variables.py
usuarioAdmin = "Ignacio123"
passwordAdmin = "ContraseñaSegura456"
edad = 30 
altura = 1.76
estaCasado = True
#String en bloques de texto
mensajeEnBloque = """Este es un mensaje de varias líneas.
Puede contener saltos de línea y 
otros caracteres especiales."""
print(mensajeEnBloque)

print("Usuario Admin:", usuarioAdmin)
print("Contraseña Admin:", passwordAdmin)
print("Edad:", edad)
print("Altura:", altura)
print("Está Casado:", estaCasado)

#convertir datos
stringEdad = str(edad)
stringAltura = str(altura)
stringEstaCasado = str(estaCasado)

#convertir strings a otros tipos de datos
intEdad = int(stringEdad)
floatAltura = float(stringAltura)
boolEstaCasado = bool(stringEstaCasado)

#introducir datos por consola
nombre = input("Ingrese su nombre: ") #Siempre devuelve un string, aunque se ingrese un número
print(type(nombre)) #muestra el tipo de dato de la variable
print("Hola, " + nombre + "!")

#otra forma de concatenar es formatear la cadena con f-strings
print(f"Hola, {nombre}!")

URL = "https://www.example.com"  #constantes con mayúsculas

num1 = 4.56
num2 = 3
modulo = num1 % num2
print(f"El módulo de {num1} y {num2} es: {modulo}")

