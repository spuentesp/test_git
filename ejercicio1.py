# Solicitar el nombre de la persona
nombre = input("Por favor, ingresa tu nombre: ")

# Mostrar las opciones de saludo

print("1. Hola")
print("2. Adiós")

# Bucle para validar la selección del usuario
while True:
    opcion = input("Elige una opción (1 o 2): ").strip()
    
    if opcion == "1":
        print(f"\n¡Hola!")
        break
    elif opcion == "2":
        print(f"\n¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, escribe 1 o 2.")