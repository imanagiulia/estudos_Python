# arquivo responsável pela validação dos dados

from pydantic import BaseModel

class EstudanteBase(BaseModel):
    nome: str
    idade: int

class EstudanteCreate(EstudanteBase):
    pass

class EstudanteResponse(EstudanteBase):
    id: int
    class Config:
        from_attributes = True # indica que pode ler as informações direto do modelo
class MatriculaBase(BaseModel):
    estudante_id: int
    nome: str

class MatriculaCreate(MatriculaBase):
    pass

class MatriculaResponse(MatriculaBase):
    id: int
    class Config:
        from_attributes = True