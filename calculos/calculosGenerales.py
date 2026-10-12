def suma(a,b):
    return print("La suma de", a, "y", b, "es:", a + b)

def resta(a,b):
    return print("La resta de", a, "y", b, "es:", a - b)

def multiplicacion(a,b):
    return print("La multiplicación de", a, "y", b, "es:", a * b)

def division(a,b):
    if b == 0:
        return print("Error: No se puede dividir por cero.")
    return print("La división de", a, "y", b, "es:", a / b) 

def redondear(a):
    return print("El número", a, "redondeado es:", round(a))

