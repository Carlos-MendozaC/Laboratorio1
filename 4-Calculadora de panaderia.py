def mostrar_menu():
    print("\nMenú:")
    print("1. Calcular el coste de barras de pan")
    print("2. Salir")

def calcular_coste():

    precio_habitual = 3.49

    descuento = 0.60

    num_barras = int(input("Ingrese el número de barras de pan que son de un dia anterior: "))

    precio_descuento = precio_habitual * (1 - descuento)

    coste_total = precio_descuento * num_barras

    print(f"\nPrecio habitual de una barra de pan: {precio_habitual} pesos")
    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Precio con descuento: {precio_descuento:.2f} pesos")
    print(f"Coste total para {num_barras} barras: {coste_total:.2f} pesos")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1 o 2): ")

        if opcion == "1":
            calcular_coste()
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()
    
