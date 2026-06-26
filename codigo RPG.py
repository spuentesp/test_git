
# 1. Solicitar el nombre del jugador
nombre = input("Ingresa el nombre de tu personaje: ").strip()

# 2. Definir las opciones disponibles
roles = {
    "1": "Héroe (Protector de la luz)",
    "2": "Villano (Señor de la oscuridad)",
    "3": "Anti-héroe (Justiciero solitario)"
}

clases = {
    "1": "Guerrero (Fuerza y acero)",
    "2": "Mago (Hechizos y misterio)",
    "3": "Pícaro (Sigilo y agilidad)"
}

# 3. Selección del Rol
print(f"\n--- BIENVENIDO, {nombre.upper()} ---")
print("Selecciona tu ROL:")
for clave, valor in roles.items():
    print(f"{clave}. {valor}")

while True:
    eleccion_rol = input("Elige el número de tu rol: ").strip()
    if eleccion_rol in roles:
        rol_elegido = roles[eleccion_rol]
        break
    print("Opción no válida. Por favor, elige un número de la lista.")

# 4. Selección de la Clase
print("\nSelecciona tu CLASE:")
for clave, valor in clases.items():
    print(f"{clave}. {valor}")

while True:
    eleccion_clase = input("Elige el número de tu clase: ").strip()
    if eleccion_clase in clases:
        clase_elegido = clases[eleccion_clase]
        break
    print("Opción no válida. Por favor, elige un número de la lista.")

# 5. Resultado Final
print("\n" + "="*40)
print(f"¡FICHA DE PERSONAJE CREADA!")
print(f"Nombre: {nombre}")
print(f"Rol:    {rol_elegido}")
print(f"Clase:  {clase_elegido}")
print("="*40)
