def calcular_capital(cantidad_invertir, interes_anual, num_anios):
    for ano in range(1, num_anios + 1):
        capital = cantidad_invertir * (1 + interes_anual / 100) ** ano
        print(f"Año {ano}: Capital acumulado = {capital:.2f} pesos")

def menu():
    while True:
        print("\nMenú:")
        print("1. Ingresar cantidad a invertir")
        print("2. Salir")

        opcion = input("Elige una opción (1 o 2): ")

        if opcion == "1":
            try:
                cantidad_invertir = float(input("Introduce la cantidad a invertir: "))
                interes_anual = float(input("Introduce el interés anual (en %): "))
                num_anios = int(input("Introduce el número de años: "))
                calcular_capital(cantidad_invertir, interes_anual, num_anios)
            except ValueError:
                print("Por favor, introduce valores válidos.")
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")

menu()

