#persistencia de datos
# Manejo de archivos externos
# Los fases para guardar información en archivo externo son:
#1. Creación del archivo externo
#2. Apertura del archivo externo
#3. Manipulación del archivo externo
#4. Cierre del archivo externo

#Trabajamos con el módulo I/O de Python para manejar archivos externos. Este módulo nos permite abrir, leer, escribir y cerrar archivos de manera sencilla.

#Los métodos más comunes para trabajar con archivos son open(), read(), write() y close(). 
#Otros métodos útiles son readline() y readlines() para leer líneas individuales o todas las líneas de un archivo, respectivamente.
# Además, podemos utilizar el módulo pickle para guardar y cargar objetos de Python en archivos binarios.
from io import open

archivoExterno = open("archivo.txt", "w") 
# El primer parámetro es el nombre del archivo y el segundo parámetro es el modo de apertura. 
# En este caso, "w" significa que abrimos el archivo en modo escritura.
# Abrimos el archivo en modo escritura ("w"). Si el archivo no existe, se crea. Si existe, se sobrescribe.
# También se puede abrir en modo lectura ("r") o en modo anexado ("a"), entre otros.
# Es importante cerrar el archivo después de manipularlo para liberar recursos del sistema.
frase = "Hola, este es un ejemplo de cómo guardar información en un archivo externo.\nLineaa 2: Esta es otra línea de texto.\nLinea 3: Y esta es la última línea de texto."
archivoExterno.write(frase) # Escribimos la frase en el archivo externo.
archivoExterno.close() # Cerramos el archivo que abrimos en memoria, o sea el archivo que se llama archivoExterno.

print("Se ha guardado la información en el archivo externo 'archivo.txt'.")
print("El archivo se encuentra en la misma carpeta que este script. Puedes abrirlo para ver el contenido.")

