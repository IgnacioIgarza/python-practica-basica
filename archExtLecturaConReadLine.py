from io import open
import pickle

archivo_texto = open("archivo.txt", "r") # Abrimos el archivo en modo lectura ("r"). Si el archivo no existe, se genera un error.
linea = archivo_texto.readline() # Leemos la primera línea del archivo externo y la guardamos en la variable linea.
print("La primera línea del archivo externo es:")
print(linea)
archivo_texto.seek(0) # Movemos el puntero del archivo al inicio del archivo para poder leer la segunda línea.
textoDelArchivoExterno = archivo_texto.read() # Leemos el contenido del archivo externo y lo guardamos en la variable textoDelArchivoExterno.
print("El contenido del archivo externo es:")
print(textoDelArchivoExterno)
archivo_texto.close() # Cerramos el archivo que abrimos en memoria, o sea el archivo que se llama archivo_texto.
