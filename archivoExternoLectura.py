# Leemos el archivo externo que creamos en el archivo archivoExternoCreacion.py
# Abrimos el archivo en modo lectura ("r"). Si el archivo no existe, se genera un error.
from io import open


archivoExterno = open("archivo.txt", "r") # El primer parámetro es el nombre del archivo 
# y el segundo parámetro es el modo de apertura. 
#En este caso, "r" significa que abrimos el archivo en modo lectura.

textoDelArchivoExterno = archivoExterno.read() # Leemos el contenido del archivo externo y lo guardamos en la variable textoDelArchivoExterno.

lineasDelArchivoExterno = archivoExterno.readlines() # Leemos el contenido del archivo externo y lo guardamos en la variable lineasDelArchivoExterno.
# Pero la lista está vacía porque ya leímos el contenido del archivo externo con el método read() y el puntero del archivo está al final del archivo.

archivoExterno.close() # Cerramos el archivo que abrimos en memoria, o sea el archivo que se llama archivoExterno.

print("El contenido del archivo externo 'archivo.txt' es:")
print(textoDelArchivoExterno)
print("")
print("El contenido del archivo externo 'archivo.txt' separado en líneas es:")
print(lineasDelArchivoExterno)
print("")
print(textoDelArchivoExterno.split("\n")) # Separamos el contenido del archivo externo en líneas y lo guardamos en una lista.
print("")
# Imprimimos solo la segunda línea del archivo externo.
print("La segunda línea del archivo externo es:")
print(textoDelArchivoExterno.split("\n")[1])
# Explicación de la linea anterior: textoDelArchivoExterno.split("\n") separa el contenido del archivo externo en líneas y lo guarda en una lista.

