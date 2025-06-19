import json

agenda = {}
contador = 1

while True:
    nombre = input(f"Ingrese el nombre del contacto {contador}: ").strip().capitalize()
   
    # Validación del teléfono
    while True:
        try:
            telefono = int(input("Ingrese el número de teléfono: "))
            break
        except ValueError:
            print("Número de teléfono inválido. Intente de nuevo.")
            
    # Validación del correo electrónico        
    while True:
        email = input("Ingrese el correo electronico: ").strip()
        if "@" in email:
            break
        else:
            print("Correo electronico inválido. Intente de nuevo.")
            
    agenda[f"contacto{contador}"] = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
            
    continuar = input("¿Desea agregar otro contacto? (s/n): ").strip().lower()
    if continuar != 's':
        break
    contador += 1
    
# Guardar la agenda en un archivo JSON
with open("agenda.json", "w") as archivo:
    json.dump(agenda, archivo, indent=4)
print("Agenda guardada en 'agenda.json'.")

# Cargar la agenda desde el archivo JSON
with open("agenda.json", "r") as archivo:
    agenda_cargada = json.load(archivo)
print("Agenda cargada desde 'agenda.json':")

# Leer y mostrar los contactos
for clave, contacto in agenda_cargada.items():
    print(f"{clave}:")
    print(f"  Nombre: {contacto['nombre']}")
    print(f"  Teléfono: {contacto['telefono']}")
    print(f"  Email: {contacto['email']}")
    print() # Línea en blanco para mejor legibilidad
# Fin del programa
            