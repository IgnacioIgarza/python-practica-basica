listaNombres = ["Juan", "María", "Pedro", "Ana", "Luis"]
print(listaNombres[0])  # Imprime el primer nombre de la lista
print(listaNombres[2])  # Imprime el tercer nombre de la lista
print(listaNombres[-3])  # Imprime el tercer nombre de la lista contando desde el final
print(listaNombres[1:4])  # Imprime los nombres desde el índice 1 hasta el índice 3
print(listaNombres[:3])  # Imprime los primeros tres nombres de la lista
print(listaNombres[2:])  # Imprime los nombres desde el índice 2 hasta el final de la lista
listaNombres.append("Sofía")  # Agrega un nuevo nombre al final de la lista

print(listaNombres)  # Imprime la lista completa con el nuevo nombre agregado

def imprimir_lista(lista):
    print()
    print("**Elementos en la lista:**")
    for nombre in lista:
        print(lista.index(nombre)+1, "- ", nombre)  # Imprime el índice y el nombre de cada elemento en la lista

imprimir_lista(listaNombres)  # Llama a la función para imprimir la lista de nombres

if "Ana" in listaNombres:
    print("Ana está en la lista.")
    print("Índice de Ana:", listaNombres.index("Ana"))
    
listaNombres.remove("Pedro")  # Elimina el nombre "Pedro" de la lista
print("Lista después de eliminar a Pedro:", listaNombres)  # Imprime la lista
listaNombres.pop(1)  # Elimina el nombre en el índice 1 (María) de la lista
print("Lista después de eliminar a María:", listaNombres)  # Imprime la lista
listaNombres.pop()  # Elimina el último nombre de la lista
print("Lista después de eliminar el último nombre:", listaNombres)  # Imprime la lista

imprimir_lista(listaNombres)  # Llama a la función para imprimir la lista de nombres después de eliminar a Pedro

listaNombres.sort()  # Ordena la lista alfabéticamente
imprimir_lista(listaNombres)  # Llama a la función para imprimir la lista de nombres ordenada

listaNombres.insert(2, "Carlos")  # Inserta el nombre "Carlos" en la posición 2 de la lista
imprimir_lista(listaNombres)  # Llama a la función para imprimir la lista de nombres después de insertar a Carlos

listaNombres.extend(["Lucía", "Diego"])  # Agrega varios nombres al final de la lista
imprimir_lista(listaNombres)  # Llama a la función para imprimir la lista de nombres después de agregar Lucía y Diego

lista2 = ["Elena", "Fernando", 5, 10.5, True]  # Crea una nueva lista con diferentes tipos de elementos
imprimir_lista(lista2)  # Llama a la función para imprimir la nueva lista
lista3 = listaNombres + lista2  # Combina las dos listas en una nueva lista
imprimir_lista(lista3)  # Llama a la función para imprimir la lista combinada