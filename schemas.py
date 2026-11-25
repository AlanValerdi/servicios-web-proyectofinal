# CREAR CONTRATOS

from datetime import datetime

from pydantic import BaseModel

class UsuarioBaseModel(BaseModel):
    nombre: str
    password: str

class AutorBaseModel(BaseModel):
    nombre: str  

class PrestamoBaseModel(BaseModel):
    usuario: int
    libro: int

class LibroBaseModel(BaseModel):
    id_autor: int 
    titulo: str
    cantidad: int

