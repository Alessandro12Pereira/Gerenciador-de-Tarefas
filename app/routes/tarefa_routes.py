from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.database import SessionLocal
from app.schemas.tarefa_schema import TarefaCreate, TarefaResponse
from app.repositories.tarefa_repository import TarefaRepository
from app.services.tarefa_service import TarefaService

router = APIRouter(prefix="/tarefas", tags=["Tarefas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TarefaResponse])
def listar_tarefas(db: Session = Depends(get_db)):
    repository = TarefaRepository(db)
    service = TarefaService(repository)
    return service.listar_todas()

@router.post("/", response_model=TarefaResponse, status_code=status.HTTP_201_CREATED)
def criar_tarefas(tarefa: TarefaCreate, db: Session = Depends(get_db)):
    repository = TarefaRepository(db)
    service = TarefaService(repository)
    try:
        return service.criar(tarefa)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{id}", response_model=TarefaResponse)
def buscar_tarefa(id: int, db: Session = Depends(get_db)):
    repository = TarefaRepository(db)
    service = TarefaService(repository)
    try:
        return service.buscar_por_id(id)
    except Exception:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@router.put("/{id}", response_model=TarefaResponse)
def atualizar_tarefa(id: int, tarefa_dados: TarefaCreate, db: Session = Depends(get_db)):
    repository = TarefaRepository(db)
    service = TarefaService(repository)
    
    tarefa_atualizada = service.atualizar(id, tarefa_dados)
    if not tarefa_atualizada:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa_atualizada

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(id: int, db: Session = Depends(get_db)):
    repository = TarefaRepository(db)
    service = TarefaService(repository)
    
    sucesso = service.deletar(id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return
 