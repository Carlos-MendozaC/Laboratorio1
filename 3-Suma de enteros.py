def suma_enteros(n):
    return n * (n + 1) // 2

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Calcular la suma de enteros desde 1 hasta n")
        print("2. Salir")
        
        opcion = input("Elige una opción (1 o 2): ")
        
        if opcion == "2":
            print("¡Hasta luego!")
            break
        
        if opcion == "1":
            try:
                n = int(input("Introduce un entero positivo: "))
                if n <= 0:
                    print("Por favor, introduce un número entero positivo.")
                    continue
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número entero.")
                continue

            resultado = suma_enteros(n)
            print(f"La suma de todos los enteros desde 1 hasta {n} es: {resultado}")
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    menu()
