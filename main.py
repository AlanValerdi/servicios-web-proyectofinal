from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from time import process_time_ns

from peewee import Model, CharField, DateTimeField, IntegerField, PrimaryKeyField

from database import database as connection
from database import Usuario, Libro, Prestamo, Autor

from fastapi import FastAPI, HTTPException


from uvicorn import lifespan

from schemas import LibroBaseModel, UsuarioBaseModel, AutorBaseModel, PrestamoBaseModel

@asynccontextmanager
async def ciclo_de_vida(app: FastAPI):
    print("El servidor está iniciando...")
    if connection.connect(reuse_if_open=True):
        print("Conexión con la base de datos exitosa")
        connection.create_tables([Usuario, Libro, Prestamo, Autor])

    else:
        print("Algo salió mal con la base de datos")

    yield

    if connection.close():
        print("Se cerró la conexión de base de datos")
    else:
        print("Algo salió mal con la base de datos")
    print( "El servidor está finalizando...")

app = FastAPI(
    title="Proyecto Libreria - Servicios Web",
    description="API para una libreria",
    version="1.0",
    lifespan=ciclo_de_vida,
)

# Deprecado
# @app.on_event("startup")
# @app.on_ecent("shutdown")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {"message": "API para administrar una libreria"}


# USUARIO
#FUNCION POST
@app.post("/usuario")
async def crear_usuario(usuario: UsuarioBaseModel):

    usuario = Usuario.create(
        nombre = usuario.nombre,
        password = usuario.password,
    )

    return {"usuario_id": usuario.id}

#FUNCION GET
@app.get("/usuario/{id}")
async def obtener_usuario(id: int):
    usuario = Usuario.get_or_none(Usuario.id == id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"id":usuario.id, "nombre":usuario.nombre}

#FUNCION GET USUARIOS
@app.get("/usuarios")
async def obtener_usuarios():
    usuarios = Usuario.select()

    return [
        {"id": usuario.id, "nombre": usuario.nombre}
        for usuario in usuarios
    ]
#FUNCION PUT
@app.put("/usuario/{id}")
async def actualizar_usuario(id: int,usuario_actualizado: UsuarioBaseModel):
    usuario = Usuario.get_or_none(Usuario.id == id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.nombre = usuario_actualizado.nombre
    usuario.password = usuario_actualizado.password
    usuario.save()

    return {
        "id": usuario.id,
        "nombre": usuario.nombre,
        "mensaje": "Usuario actualizado con exito"
    }
#FUNCION DELETE
@app.delete("/usuario/{id}")
async def eliminar_usuario(id: int):
    usuario = Usuario.get_or_none(Usuario.id == id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.delete_instance()

    return {
        "id": usuario.id,
        "nombre": usuario.nombre,
        "mensaje": "Usuario eliminado con exito"
    }

# Autor
# POST
@app.post('/autor')
async def crear_autor(autor: AutorBaseModel):

    autor = Autor.create(
        nombre = autor.nombre
    )
    return {"id_autor": autor.id ,"nombre_autor": autor.nombre}

# GET
@app.get("/autor/{id}")
async def obtener_autor(id: int):
    autor = Autor.get_or_none(Autor.id == id)
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return {"id": autor.id, "nombre_autor": autor.nombre}

@app.get("/autores")
async def obtener_autores():
    autores = Autor.select()

    return [
        {"id": autor.id, "nombre": autor.nombre}
        for autor in autores
    ]

# PUT
@app.put("/autor/{id}")
async def actualizar_autor(id: int, autor_actualizado: AutorBaseModel):
    autor = Autor.get_or_none(Autor.id == id)
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    autor.nombre = autor_actualizado.nombre
    autor.save()

    return {
        "id": autor.id,
        "nombre": autor.nombre,
        "mensaje": "Autor actualizado con exito"
    }

# DELETE
@app.delete("/autor/{id}")
async def eliminar_autor(id: int):
    autor = Autor.get_or_none(Autor.id == id)
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    autor.delete_instance()

    return {
        "id": autor.id,
        "nombre": autor.nombre,
        "mensaje": "Autor eliminado con exito"
    }

# LIBRO
#FUNCION POST
@app.post("/libro")
async def crear_libro(libro: LibroBaseModel):

    autor = Autor.get_or_none(Autor.id == libro.id_autor)

    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no existe")

    libro = Libro.create(
        autor = autor,
        titulo = libro.titulo,
        cantidad = libro.cantidad
    )

    return {"id_libro": libro.id, 
            "id_autor": autor.id,
            "titulo": libro.titulo, 
            "cantidad": libro.cantidad,
            "mensaje": "Libro registrado correctamente" }

#FUNCION GET
# GET
@app.get("/libro/{id}")
async def obtener_libro(id: int):
    libro = Libro.get_or_none(Libro.id == id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"id_libro": libro.id, 
                "id_autor": libro.autor.id, 
                "titulo": libro.titulo, 
                "cantidad": libro.cantidad,}

@app.get("/libros")
async def obtener_libros():
    libros = Libro.select()

    return [
       {"id_libro": libro.id, 
        "id_autor": libro.autor.id, 
        "titulo": libro.titulo, 
        "cantidad": libro.cantidad,}
    for libro in libros
    ]
# PUT
@app.put("/libro/{id}")
async def actualizar_libro(id: int, libro_actualizado: LibroBaseModel):
    libro = Libro.get_or_none(Libro.id == id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    autor = Autor.get_or_none(Autor.id == libro_actualizado.id_autor)
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    libro.titulo = libro_actualizado.titulo
    libro.autor = autor
    libro.cantidad = libro_actualizado.cantidad
    libro.save()

    return {
        "id_libro": libro.id, 
        "id_autor": libro.autor.id, 
        "titulo": libro.titulo, 
        "cantidad": libro.cantidad,
        "mensaje": "Libro actualizado correctamente"
    }
# DELETE
@app.delete("/libro/{id}")
async def eliminar_libro(id: int):
    libro = Libro.get_or_none(Libro.id == id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    prestamo = Prestamo.select().where(Prestamo.libro == libro).exists()
    if prestamo:
        raise HTTPException(status_code=409, detail="No se puede eliminar el libro porque tiene prestamos asociados")


    libro.delete_instance()

    return {
            "id_libro": libro.id, 
            "id_autor": libro.autor.id, 
            "titulo": libro.titulo, 
            "cantidad": libro.cantidad,
            "mensaje": "Libro borrado correctamente"
    }


# Prestamos
@app.post("/prestamo")
async def crear_prestamo(prestamo: PrestamoBaseModel):


    if Usuario.get_or_none(Usuario.id == prestamo.usuario) is None:
        raise HTTPException(status_code=404, detail="Id del usuario no encontrado")

    libro = Libro.get_or_none(Libro.id == prestamo.libro)
    if libro is None:
        raise HTTPException(status_code=404, detail="Id del libro no encontrado")
    
    if libro.cantidad <= 0:
        raise HTTPException(status_code=409, detail="El libro ya no tiene existencias")
    
    ya_prestado = Prestamo.get_or_none(
            (Prestamo.libro == prestamo.libro) &
            (Prestamo.usuario == prestamo.usuario) &
            (Prestamo.activo == True)
        )
    
    if ya_prestado is not None:
        raise HTTPException(status_code=409, detail=" El usuario ya tiene activo un prestamo de este libro")

    
    nuevo_prestamo = Prestamo.create(
        usuario = prestamo.usuario,
        libro = prestamo.libro,
        actualizado_en = datetime.now(),
        activo = True,
        fecha_limite = datetime.now() + timedelta(weeks=2),
        fecha_devolucion = None,
    )

    libro.cantidad -= 1
    libro.save()

    return {"id_prestamo": nuevo_prestamo.id, "id_usuario": nuevo_prestamo.usuario, "fecha_limite": nuevo_prestamo.fecha_limite, "mensaje": "Prestamo Creado Correctamente"}

@app.patch("/prestamo/{id}/renovar")
async def renovar_prestamo(id: int):

    prestamo = Prestamo.get_or_none(Prestamo.id == id)
    if prestamo is None:
        raise HTTPException(status_code=404, detail="El prestamo no se ha encontrado")

    if prestamo.activo is False:
        raise HTTPException(status_code=409, detail="El prestamo que se ha intentado renovar ya no se encuentra activo")

    fecha_anterior = prestamo.fecha_limite
    prestamo.fecha_limite += timedelta(weeks=1)
    prestamo.save()

    return{"id": prestamo.id, "libro": prestamo.libro, "usuario": prestamo.usuario, "fecha_anterior": fecha_anterior, "nueva_fecha": prestamo.fecha_limite, "mensaje": "Prestamo renovado correctamente"}

@app.patch("/prestamo/{id}/devolver")
async def devolver_prestamo(id: int):

    prestamo = Prestamo.get_or_none(Prestamo.id == id)
    if prestamo is None:
        raise HTTPException(status_code=404, detail="El prestamo no se ha encontrado")

    if prestamo.activo is False:
        raise HTTPException(status_code=409, detail="El prestamo que se ha intentado devolver ya no se encuentra activo")
    
    libro = Libro.get_or_none(Libro.id == prestamo.libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="El libro no se ha encontrado")
    

    prestamo.activo = False
    prestamo.fecha_devolucion = datetime.now()
    prestamo.actualizado_en = datetime.now()
    prestamo.save()

    libro.cantidad += 1
    libro.save()

    return{
        "id": prestamo.id,
        "id_libro": prestamo.libro,
        "id_usuario": prestamo.usuario,
        "mensaje": "Prestamo de devuelto con exito"
    }


@app.get("/prestamo/{id}")
async def obtener_prestamo(id: int):
    prestamo = Prestamo.get_or_none(Prestamo.id == id)
    if prestamo is None:
        raise HTTPException(status_code=404, detail="El prestamo no se ha encontrado")

    return{
        "id": prestamo.id,
        "libro": prestamo.libro, 
        "usuario": prestamo.usuario, 
        "fecha_limite": prestamo.fecha_limite, 
        "activo": prestamo.activo, 
        "fecha_devolucion": prestamo.fecha_devolucion
    }


@app.get("/prestamos")
async def obtener_prestamos():

    prestamos = Prestamo.select()

    return [
        {"id": prestamo.id, 
         "libro": prestamo.libro, 
         "usuario": prestamo.usuario, 
         "fecha_limite": prestamo.fecha_limite, 
         "activo": prestamo.activo, 
         "fecha_devolucion": prestamo.fecha_devolucion}
        for prestamo in prestamos
    ]


    