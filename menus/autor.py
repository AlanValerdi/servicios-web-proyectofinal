from menus.utils import URL_SERVER, pedir_opcion, pedir_id

import requests

def crear_autor():
    nombre = input("\n Ingresa el nombre del nuevo autor \n").strip()
    respuesta = requests.post(f"{URL_SERVER}/autor", json={"nombre": nombre})
    if respuesta.status_code == 200:
        print("Autor Creado con éxito", respuesta.json())
    else:
        print(f"Error al crear {respuesta.status_code}: ", respuesta.text)

def mostrar_autor():
    pass

def mostrar_menu_autor():
    opcion = 0
    while opcion != 6:
        print("\n --- Menú Autor --- \n")
        print(" 1 - Mostrar Autor por ID \n 2 - Mostrar Todos los autores \n 3 - Crear Autor \n 4 - Editar Autor \n 5 - Eliminar Autor \n 6 - Volver al menú principal \n")
        opcion = pedir_opcion()

        if opcion == 3:
            crear_autor()