contraseña_correcta = "contraseña"

while True:
    print("\nMenú:")
    print("1. Introducir contraseña")
    print("2. Salir")
    
    opcion = input("Selecciona una opción (1 o 2): ")
    
    if opcion == "1":
        contraseña_usuario = input("Introduce la contraseña: ")
        if contraseña_usuario == contraseña_correcta:
            print("Contraseña correcta. Acceso concedido.")
            break
        else:
            print("Contraseña incorrecta. Inténtalo de nuevo.")
    elif opcion == "2":
            print("Saliendo del programa.")
            break
    else:
        print("Opción no válida. Por favor, selecciona 1 o 2.")
                
           
               
