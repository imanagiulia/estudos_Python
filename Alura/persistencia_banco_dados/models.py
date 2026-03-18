#Modelagem das entidades 

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Estudante(Base):
    __tablename__ = 'estudantes'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    perfil = relationship(
        "Perfil", 
        back_populates="estudante",
        uselist=False, #relação 1:1
        cascade="all, delete-orphan" # all -> todos os filhos de estudante tbm serão afetados / delete-orphan -> se um estudante for deletado o perfil vinculado a ele tbm será
    ) #Cria uma relação entre estudante e perfil

class Perfil(Base):
    __tablename__ = 'perfis'
    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String)
    estudante_id = Column(
        Integer,
        ForeignKey('estudantes.id', unique=True)
    )
    estudante = relationship(
        "Estudante",
        back_populates = "perfil"
    )