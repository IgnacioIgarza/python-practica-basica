print("Programa de becas 2026")
derechoABeca = False

distancia = int(input("Ingrese la distacia a la escuela "))
print(f"La distancia a la escuela es de {distancia} Km.")
hermanos = int(input("Ingrese el número de hermanos "))
print(f"La cantidad de hermanos del alumno es {hermanos}.")
salario = int(input("Ingrese el salario familiar anual "))
print(f"El salario familiar es de ${salario} anuales.")

if distancia > 40 and hermanos > 2 or salario < 20000:
    derechoABeca = True
    print("*El alumno tiene derecho a beca.")
else:
    print("*El alumno no tiene derecho a beca.")
    
    
    
if derechoABeca:
    print()
    
    print("Elija una de las siguientes opcionesde asignaturas:")
    print("a. Matemáticas")
    print("b. Física")
    print("c. Química")
    
    opcion = input("Ingrese la letra de la asignatura que desea inscribirse: ")
    inscripcion = opcion.lower()
    if inscripcion in ["a", "b", "c"]:
        print(f"El alumno se ha inscrito en la asignatura {inscripcion}.")  
    else:
        print("Opción inválida. Por favor, elija una opción válida (a, b o c).")
    