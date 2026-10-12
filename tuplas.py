# Tuplas en Python
# Una tupla es una colección de elementos que no se pueden modificar después de su creación. 
# Se definen utilizando paréntesis () y pueden contener elementos de diferentes tipos de datos.
# No admiten los métodos de modificación como append(), remove() o pop() que sí están disponibles para las listas.
# Utilidad: Las tuplas son útiles cuando se desea almacenar un conjunto de elementos que no deben cambiar a lo largo del tiempo, como coordenadas, fechas, o cualquier otro tipo de datos que se consideren constantes.
miTupla = (1, 4 , "Hola", 3.14, True)
# Acceder a los elementos de una tupla
print(miTupla[0])  # Imprime el primer elemento: 1
# Acceder a los elementos de una tupla con un for loop
for elemento in miTupla:
    print(elemento)
    