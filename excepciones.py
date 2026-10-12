#Excepciones para manejo de errores inesperados
try:
    print("Vamos a dividir 10 entre 0")
    print(10/0)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
    
print("**"*20)
print("Continuamos con el programa")

def dividir(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return None

num1 = (int(input("Introduce el primer numero: ")))
num2 = (int(input("Introduce el segundo numero: ")))
print(dividir(num1, num2))

print("**"*20)
print("Continuamos con el programa")
