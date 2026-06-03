from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from database import Base, engine
from database import SessionLocal
from sqlalchemy.orm import Session 
import models

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Tarefa(BaseModel):
    titulo: str
    descricao: str
    concluida: bool

app = FastAPI()

tarefas = []
contador_id = 1

@app.get("/")
def home():
    return{"mensagem": "API funcionando"}

@app.get("/tarefas")
def listar_tarefas(db: Session = Depends(get_db)):
    tarefas = db.query(models.Tarefas).all()
    return tarefas

@app.post("/tarefas")
def criar_tarefa(titulo:str, descricao: str, db: Session = Depends(get_db)):
    nova_tarefa = models.Tarefas(
        titulo = titulo,
        descricao = descricao,
        concluida = False
    )
    
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    
    return nova_tarefa

@app.get("/tarefas/{id}")
def buscar_tarefa(id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefas).filter(models.Tarefas.id == id).first()
    
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    return tarefa

@app.put("/tarefas/{id}")
def atualizar_tarefa(
    id: int,
    titulo: str,
    descricao: str,
    concluida: bool,
    db: Session = Depends(get_db)
):
    
    if tarefa:
        raise HTTPException(status_code=404,detail="Tarefa não encontrada")
    
    
    tarefa.titulo = titulo
    tarefa.descricao = descricao
    tarefa.concluida = concluida
    
    db.commit()
    db.refresh(tarefa)
    
    return tarefa

@app.delete("/tarefas/{id}")
def deletar_tarefas(id:int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefas).filter(models.Tarefa.id == id).first()
    if not tarefa:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )
    db.delete(tarefa)
    db.commit
    
    return{"mensagem":"Tarefa deletada com sucesso"}
