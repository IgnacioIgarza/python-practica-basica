# Aqui se importan los modulos de calculosGenerales.py de la carpeta calculos.
# Para eso, la carpeta calculos debe contener un archivo __init__.py para que Python la reconozca como un paquete.

from calculos.calculosGenerales import * # Se pueden especificar las funciones a importar, pero en este caso se importan todas.

suma(5, 3)
resta(5, 3)
multiplicacion(5, 3)
division(5, 0)
redondear(3.7)
