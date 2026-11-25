from menus.utils import URL_SERVER, pedir_opcion, pedir_id

import requests

def mostrar_libro():

    id = pedir_id("\n Ingresa el ID del libro que quieres consultar: \n")

    respuesta = requests.get(f"{URL_SERVER}/libro/{id}")

    if respuesta.status_code == 200:
        print("\n Información del libro: \n", respuesta.json())
    else:
        print(f"\n Error al obtener información: {respuesta.status_code}: ", respuesta.text)

def mostrar_libros():

    respuesta = requests.get(f"{URL_SERVER}/libros")

    if respuesta.status_code == 200:
        print("\n Listado de libros: \n", respuesta.json())
    else:
        print(f"\n Error al obtener libros: {respuesta.status_code}: ", respuesta.text)

def crear_libro():

    id_autor = pedir_id("\n Ingresa el ID del autor del libro: \n")
    titulo = input("\n Ingresa el titulo del libro: \n").strip()
    cantidad = int(input("\n Ingresa la cantidad de ejemplares: \n"))

    respuesta = requests.post(
        f"{URL_SERVER}/libro",
        json={
            "id_autor": id_autor,
            "titulo": titulo,
            "cantidad": cantidad
        }
    )

    if respuesta.status_code == 200:
        print("\n Libro creado con éxito \n", respuesta.json())
    else:
        print(f"\n Error al crear libro: {respuesta.status_code}: ", respuesta.text)

def modificar_libro():

    id = pedir_id("\n Ingresa el ID del libro que quieres modificar: \n")

    id_autor = pedir_id("\n Ingresa el nuevo ID del autor: \n")
    nuevo_titulo = input("\n Ingresa el nuevo titulo del libro: \n").strip()
    nueva_cantidad = int(input("\n Ingresa la nueva cantidad de ejemplares: \n"))

    respuesta = requests.put(
        f"{URL_SERVER}/libro/{id}",
        json={
            "id_autor": id_autor,
            "titulo": nuevo_titulo,
            "cantidad": nueva_cantidad
        }
    )

    if respuesta.status_code == 200:
        print("\n Libro actualizado con éxito: ", respuesta.json())
    else:
        print(f"\n Error al modificar libro: {id}, {respuesta.status_code}: ", respuesta.text)

def eliminar_libro():

    id = pedir_id("\n Ingresa el ID del libro que quieres eliminar: \n")

    respuesta = requests.delete(f"{URL_SERVER}/libro/{id}")

    if respuesta.status_code == 200:
        print("\n Libro eliminado con éxito: ", respuesta.json())

    elif respuesta.status_code == 409:
        print("\n No se puede eliminar el libro porque tiene préstamos asociados: ", respuesta.text)

    else:
        print(f"\n Error al eliminar libro: {id}, {respuesta.status_code}: ", respuesta.text)

def mostrar_menu_libro():

    opcion = 0

    while opcion != 6:

        print("\n --- Menú Libro --- \n")

        print(" 1 - Mostrar Libro por ID \n 2 - Mostrar Todos los Libros \n 3 - Crear Libro \n 4 - Editar Libro \n 5 - Eliminar Libro \n 6 - Volver al menú principal \n")
        opcion = pedir_opcion()
     

        if opcion == 1:
            mostrar_libro()

        elif opcion == 2:
            mostrar_libros()

        elif opcion == 3:
            crear_libro()

        elif opcion == 4:
            modificar_libro()

        elif opcion == 5:
            eliminar_libro()

        elif opcion == 6:
            print("Volviendo al menu principal")

        else:
            print("Opcion invalida")