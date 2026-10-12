# Operaciones Simples
# Se definen funciones para realizar operaciones matemáticas básicas.
# Serán importadas y utilizadas en otros módulos.

def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def resta(a, b):
    """Devuelve la resta de dos números."""
    return a - b    

def multiplicacion(a, b):
    """Devuelve la multiplicación de dos números."""
    return a * b

def division(a, b):
    """Devuelve la división de dos números. Lanza un error si el divisor es cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def potencia(a, b):
    """Devuelve a elevado a la potencia b."""
    return a ** b

def raiz_cuadrada(a):
    """Devuelve la raíz cuadrada de un número. Lanza un error si el número es negativo."""
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return a ** 0.5

def logaritmo(a, base):
    """Devuelve el logaritmo de a en la base especificada. Lanza un error si a es menor o igual a cero o si la base es menor o igual a uno."""
    import math
    if a <= 0:
        raise ValueError("No se puede calcular el logaritmo de un número menor o igual a cero.")
    if base <= 1:
        raise ValueError("La base del logaritmo debe ser mayor que uno.")
    return math.log(a, base)