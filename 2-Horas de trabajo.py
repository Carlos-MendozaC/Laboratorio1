def calcular_paga():
    horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
    
    costo_por_hora = float(input("Ingrese el costo por hora: "))
    
    paga = horas_trabajadas * costo_por_hora
    
    print(f"La paga que le corresponde es: {paga}")

def mostrar_menu():
    print("\nMenú:")
    print("1. Calcular paga")
    print("2. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1 o 2): ")
        
        if opcion == '1':
            calcular_paga()
        elif opcion == '2':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija 1 o 2.")

if __name__ == "__main__":
    main()
