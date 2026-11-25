import requests
from menus.autor import mostrar_menu_autor
from menus.usuario import  mostrar_menu_usuario
from menus.prestamos import mostrar_menu_prestamo
from menus.libro import mostrar_menu_libro
from menus.utils import pedir_opcion

iterador: int = 0

while iterador != 5:
    print("\n Elige la entidad sobre la que quieres realizar las operaciones: \n")
    print(" 1 - Libro \n 2 - Autor \n 3 - Prestamo \n 4 - Usuario \n 5 - Salir \n")

    iterador = pedir_opcion()

    if iterador == 1:
        mostrar_menu_libro()
    elif iterador == 2:
        mostrar_menu_autor()
    elif iterador == 3:
        mostrar_menu_prestamo()
    elif iterador == 4:
        mostrar_menu_usuario()
    
    

print("\n Has salido del programa \n")