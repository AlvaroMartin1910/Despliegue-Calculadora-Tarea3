"""Calculadora sencilla de consola."""


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
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
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
