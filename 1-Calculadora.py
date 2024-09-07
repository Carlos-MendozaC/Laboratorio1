import math

def menu():
    print("\nCalculadora Aritmética")
    print("1. Realizar una operación")
    print("2. Salir")
    print("\nInstrucciones:")
    print(" - Puedes ocupar las siguientes operaciones.")
    print(" - + (suma), - (resta), * (multiplicación), / (división), ** (potencia).")
    print(" - Ejemplo de entradas:")
    print(" - ((3 + 2) / (2 * 5)) ** 2")
    re = ((3 + 2) / (2 * 5)) ** 2
    print(re)

def main():
    resultado = None

    while True:
        menu()
        opcion = input("Elige una opción (1 o 2): ")

        if opcion == '1':
            expresion = input("Introduce la operación matemática: ")
            
            try:
                
                resultado = eval(expresion, {"__builtins__": None}, {})
                print(f"El resultado de la operación es: {resultado}")
            except (SyntaxError, NameError):
                print("Error: Expresión inválida.")
            except ZeroDivisionError:
                print("Error: División por cero.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == '2':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()


