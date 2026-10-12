# Se se usan las funciones definidas en operacionesSimples.py para realizar cálculos matemáticos básicos.
# __pycache__ es un directorio que contiene archivos compilados de Python para mejorar el rendimiento de la carga de módulos.
import operacionesSimples as ops

print("Suma de 5 y 3: ", ops.suma(5, 3))
print("Resta de 5 y 3: ", ops.resta(5, 3))
print("Multiplicación de 5 y 3: ", ops.multiplicacion(5, 3))
try:
    print("División de 5 y 0: ", ops.division(5, 0))
except ValueError as e:
    print(e)
print("Potencia de 5 y 3: ", ops.potencia(5, 3))
print("Raíz cuadrada de 25: ", ops.raiz_cuadrada(25))
print("Raíz cuadrada de -25: ", end="")
try:
    print(ops.raiz_cuadrada(-25))
except ValueError as e:
    print(e)

print("División de 10 y 2: ", ops.division(10, 2))
