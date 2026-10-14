"""Calculadora sencilla de consola con validación de datos."""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a / b


def main():
    print("=== Calculadora ===")
    print("Operaciones disponibles: +  -  *  /")

    # Validación para el primer número (a)
    while True:
        try:
            a = float(input("Primer número: "))
            break  # Si la conversión es exitosa, sale del bucle
        except ValueError:
            print("Error: Las letras no son un tipo de dato válido. Por favor, introduce solo números.")

    # Validación para el segundo número (b)
    while True:
        try:
            b = float(input("Segundo número: "))
            break  # Si la conversión es exitosa, sale del bucle
        except ValueError:
            print("Error: Las letras no son un tipo de dato válido. Por favor, introduce solo números.")

    operacion = input("Operación: ")

    if operacion == "+":
        print("Resultado:", sumar(a, b))
    elif operacion == "-":
        print("Resultado:", restar(a, b))
    elif operacion == "*":
        print("Resultado:", multiplicar(a, b))
    elif operacion == "/":
        print("Resultado:", dividir(a, b))


if __name__ == "__main__":
    main()
