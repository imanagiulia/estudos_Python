# porta de entrada e saída dos dados. Define o formato exato dos dados que a API aceita receber(Requests) e devolver(response)

from typing import List, Optional
from pydantic import BaseModel

#retorna dados
class Perfil(BaseModel):
    id: int
    idade: int
    endereco: str 

    class Config:
        from_attributes = True

        """Transforma os dados vindo do banco de dados em um objeto JSON"""

#quando um usuário faz um POST
class PerfilCreate(BaseModel):
    idade: int
    endereco: str

class PerfilUpdate(BaseModel):
    idade: Optional[int] = None
    endereco: Optional[str] = None

class Estudante(BaseModel):
    id: int
    nome: str
    perfil: Optional[Perfil] = None

    class Config:
        from_attributes = True

class EstudanteCreate(BaseModel):
    nome: str 
    email: str
    perfil: PerfilCreate

class EstudanteUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    perfil: Optional[PerfilUpdate] = None
