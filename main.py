from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


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
def listar_tarefas():
    return tarefas

@app.post("/tarefas")
def criar_tarefa(tarefa:Tarefa):
    global contador_id
    
    nova_tarefa = {
        "id": contador_id,
        "titulo": tarefa.titulo,
        "descricao": tarefa.descricao,
        "concluida": tarefa.concluida
    }
    tarefas.append(nova_tarefa)
    contador += 1
    
    return nova_tarefa

@app.get("/tarefas/{id}")
def buscar_tarefa(id: int):
    if id >=len(tarefas):
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )
    return tarefas[id]

@app.put("/tarefas/{id}")
def atualizar_tarefa(id: int,tarefa: dict):
    if id >= len(tarefas):
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )
        
    tarefas[id] = tarefa
    
    return tarefa

@app.delete("/tarefas/{id}")
def deletar_tarefas(id:int):
    if id >= len(tarefas):
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )
    tarefas.pop(id)
    
    return{"mensagem":"Tarefa deletada"}
