def suma(a, b):
    return a + b

def main():
    print("=== Calculadora Colaborativa ===")
    x = float(input("Primer número: "))
    y = float(input("Segundo número: "))
    print("Suma:", suma(x, y))

if __name__ == "__main__":
    main()