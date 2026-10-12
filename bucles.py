for i in [1,"Verano", 2,"Otoño", 3,"Primavera", 4,"Invierno"]:
    print(i)
    
correo = input("Ingrese su correo gmail: ")
mail = False
for i in correo:
    if i == "@" and "gmail.com" in correo:
        mail = True
if mail:
    print("El correo electrónico es válido.")
else:
    print("El correo electrónico no es válido.")
    

for i in range(1, 11): #Los parametros de range son: inicio, fin, paso
    print(i) #Imprime los números del 1 al 10
    
for i in range(1, 11, 2): #Los parametros de range son: inicio, fin, paso
    print(i) #Imprime los números del 1 al 10 de 2 en 2
    
for i in range(10, 0, -1): #Los parametros de range son: inicio, fin, paso
    print(i) #Imprime los números del 10 al 1 de 1 en 1
    
for n in range(5): # 0, 1, 2, 3, 4
    print(n) # Imprime los números
    
lista = ["a", "b", "c"]
for n in lista:
    print(n)
    

# While
cont = 0
while cont < 4:
    print(cont)
    cont += 1

# Para salir de un bucle infinito, crtl + c que termina el programa

contraseña = ""
while contraseña != "123":
    print("Ingrese la contraseña.")
    

while True:
    print("1-HOla")
    print("0-Salir")
    opcion = input("Escriba una opcion")
    if opcion == "0":
        print("Chau!")
        break
    