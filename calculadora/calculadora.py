def ingresarNumero():
    while True:
        try:
            numero = float(input("Ingrese un número: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def ingresarOperacion():
    while True:
        operacion = input("Ingrese la operación (+, -, *, /, =): ")
        if operacion in ['+', '-', '*', '/', '=']:
            return operacion
        else:
            print("Operación inválida. Por favor, ingrese una operación válida.")

def calcular(num1, num2, operacion):
    while operacion != '=':
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            while num2 == 0:
                print("Error: División por cero no permitida.")
                num2 = ingresarNumero()
            resultado = num1 / num2
        else:
            print("Operación inválida.")
            return None

        print(f"{num1} {operacion} {num2} = {resultado}")
        num1 = resultado
        operacion = ingresarOperacion()
        if operacion != '=':
            num2 = ingresarNumero()
    return resultado

def main():
    print("**Bienvenido a la calculadora básica**")
    print("Puede realizar operaciones de suma (+), resta (-), ")
    print("multiplicación (*), y división (/).")
    print("Ingrese '=' como operación para finalizar.")
    num1 = ingresarNumero()
    operacion = ingresarOperacion()
    if operacion != '=':
        num2 = ingresarNumero()
        resultado_final = calcular(num1, num2, operacion)
        if resultado_final is not None:
            print(f"Resultado final: {resultado_final}")
    else:
        print("No se realizó ninguna operación.")
        print(f"Resultado final: {num1}")

if __name__ == "__main__":
    main()
