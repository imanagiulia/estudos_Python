# arquivo onde as rotas da aplicação (endpoints) são definidas

from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import session_local, engine

# Cria as tabelas no PostgreSQL caso não exista
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

# função que cria um novo estudante e salva ele no banco de dados
# rota que só aceita o método POST
@app.post('/estudantes/', response_model=schemas.EstudanteResponse)
def create_estudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_estudante = models.Estudante(**estudante.model_dump()) # cria um objeto do modelo Estudante com as informações que estão vindo do navegador
    db.add(db_estudante) # adiciona ao banco de dados
    db.commit() # confirma a execução
    db.refresh(db_estudante) # atualizada o banco de dados 
    return db_estudante


# função que lê as informarções do banco de dados
@app.get('/estudantes/', response_model= List[schemas.EstudanteResponse])
def read_estudantes(db: Session = Depends(get_db)):
    estudantes = db.query(models.Estudante).all() # retorna todas as ocorrências do modelo Estudantes - equivalente ao SELECT * FROM Estudantes
    return estudantes

@app.post('/matriculas/', response_model=schemas.EstudanteResponse)
def create_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    db_matricula = models.Matriculas(**matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula


@app.get('/matriculas/', response_model= List[schemas.MatriculaResponse])
def read_matriculas(db: Session = Depends(get_db)):
    matriculas = db.query(models.Matriculas).all()
    return matriculas