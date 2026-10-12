# Agregamos información al archivo externo llamado archivo.txt que creamos en el archivo archivoExternoCreacion.py
# Abrimos el archivo en modo anexado ("a"). Si el archivo no existe, se genera un error.
from io import open

archivoExterno = open("archivo.txt", "a") # El primer parámetro es el nombre del archivo y el segundo parámetro es el modo de apertura.
archivoExterno.write("\nEsta es una línea agregada al archivo.") # Escribimos la frase en el archivo externo.
archivoExterno.close() # Cerramos el archivo que abrimos en memoria, o sea el archivo que se llama archivoExterno.
print("Se ha agregado información al archivo externo 'archivo.txt'.")