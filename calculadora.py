def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def main():
    print("======= CALCULADORA COLABORATIVA =======")   # <-- línea modificada por A (diferente a la de B)
    x = float(input("Primer número: "))
    y = float(input("Segundo número: "))
    print("Suma:", suma(x, y))
    print("Resta:", resta(x, y))
    print("Multiplicación:", multiplicacion(x, y))

if __name__ == "__main__":
    main()