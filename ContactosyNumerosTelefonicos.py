def contactos_y_numeros_telefonicos():
    contactos = {}
    while True:
        nombre = input("Ingrese el nombre del contacto (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        numero = input("Ingrese el número telefónico del contacto: ")
        contactos[nombre] = numero
    return contactos
if __name__ == "__main__":    contactos = contactos_y_numeros_telefonicos()
print("\nContactos y números telefónicos:") 
for nombre, numero in contactos.items():
    print(f"{nombre}: {numero}")

   