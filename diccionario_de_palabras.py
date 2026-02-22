diccionario = {}
def agregar_palabra():
    print("\n agregar nueva palabra ")    
    palabra = input("ingrese la palabra: ").strip().lower()
    if palabra in diccionario:
        print("la palabra ya existe en el diccionario.")
        return
    significado = input("ingrese el significado: ").strip()
    if significado == "":
        print("el significado no puede estar vacio.")
        return
    diccionario[palabra] = significado
    print("palabra agregada correctamente.")
def consultar_palabra():
    print("\n consultar palabra ")    
    palabra = input("ingrese la palabra a consultar: ").strip().lower()
    if palabra in diccionario:
        print(f"📖 {palabra.capitalize()}: {diccionario[palabra]}")
    else:
        print("la palabra no se encuentra en el diccionario.")
def mostrar_diccionario():
    print("\n--- diccionario completo ---")
    if not diccionario:
        print("el diccionario esta vacio.")
    else:
        for palabra, significado in diccionario.items():
            print(f"- {palabra.capitalize()}: {significado}")
def mostrar_menu():
    print("\n diccionario de palabras ")
    print("1. agregar palabra")
    print("2. consultar palabra")
    print("3. mostrar todas las palabras")
    print("4. salir")
while True:
    mostrar_menu()
    opcion = input("seleccione una opcion: ")
    if opcion == "1":
        agregar_palabra()
    elif opcion == "2":
        consultar_palabra()
    elif opcion == "3":
        mostrar_diccionario()
    elif opcion == "4":
        print("saliendo del diccionario...")
        break
    else:
        print("opcion invalida, intente nuevamente.")