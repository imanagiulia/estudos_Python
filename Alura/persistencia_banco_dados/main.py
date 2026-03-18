from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session 
import models, schemas
from database import engine, session_local
from typing import List
from sqlalchemy.orm import joinedload

models.Base.metadata.create_all(bind=engine) # cria todas as tabelas se elas ainda não existirem

app = FastAPI()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.post('/estudantes', response_model=schemas.Estudante)
def CriarEstudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_estudante = models.Estudante(
        nome = estudante.nome,
        email = estudante.email,
        perfil = models.Perfil(**estudante.perfil.dict())
    )

    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)

    return db_estudante

@app.get('/estudante', response_model=List[schemas.Estudante])
def ListarEstudantes(db: Session = Depends(get_db)):
    estudantes = db.query(models.Estudante).options(
        joinedload(models.Estudante.perfil)
    ).all()
    
    return estudantes

@app.put('/estudantes/{estudante_id}', response_model=schemas.Estudante)
def UpdateEstudante(estudante_id: int, estudante_atualizado: schemas.EstudanteUpdate, db: Session = Depends(get_db)):
    db_estudante = db.query(models.Estudante).filter(models.Estudante.id == estudante_id).first()

    if not db_estudante:
        raise HTTPException(status_code=404, detail='Estudante não encontrado.')
    
    update_data = estudante_atualizado.dict(exclude_unset=True)

    if "nome" in update_data:
        db_estudante.nome = update_data['nome']
    if "email" in update_data:
        db_estudante.email = update_data['email']

    if "perfil" in update_data and db_estudante.perfil:
        perfil_data = update_data['perfil']
        if "idade" in perfil_data:
            db_estudante.perfil.idade = perfil_data['idade']
        if "endereco" in perfil_data:
            db_estudante.perfil.endereco = perfil_data['endereco']

    db.commit()
    db.refresh(db_estudante)
    return db_estudante

@app.delete('estudante/{estudante_id}', status_code=204)
def DeleteEstudante(estudante_id: int, db: Session = Depends(get_db)):
    db_estudante = db.query(models.Estudante).filter(models.Estudante.id == estudante_id).first()

    if not db_estudante:
        raise HTTPException(status_code=404, detail="Estudante não encontrado.")
    
    db.delete(db_estudante)
    db.commit()

    return