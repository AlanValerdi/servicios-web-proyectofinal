from datetime import datetime

from pydantic import BaseModel

class UsuarioBaseModel(BaseModel):
    nombre: str
    password: str
    creado_en: datetime

class AutorBaseModel(BaseModel):
    nombre: str  
