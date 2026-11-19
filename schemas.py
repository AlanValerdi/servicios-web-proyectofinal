# CREAR CONTRATOS

from datetime import datetime

from pydantic import BaseModel

class UsuarioBaseModel(BaseModel):
    nombre: str
    password: str

class AutorBaseModel(BaseModel):
    nombre: str  
    