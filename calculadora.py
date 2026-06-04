def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división entre cero"
    return a / b

def main():
    print("======= CALCULADORA COLABORATIVA - Version 1.0 =======")
    x = float(input("Primer número: "))
    y = float(input("Segundo número: "))
    print("Suma:", suma(x, y))
    print("Resta:", resta(x, y))
    print("Multiplicación:", multiplicacion(x, y))
    print("División:", division(x, y))

if __name__ == "__main__":
    main()

    

