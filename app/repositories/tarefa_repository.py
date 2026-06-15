from sqlalchemy.orm import Session
from app.models.tarefa import Tarefas  
class TarefaRepository:

    # Ele recebe a sessão do banco de dados na criação
    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(Tarefas).all()

    def buscar_por_id(self, tarefa_id: int):
        return self.db.query(Tarefas).filter(Tarefas.id == tarefa_id).first()

    def criar(self, tarefa: Tarefas):
        self.db.add(tarefa)
        self.db.commit()
        self.db.refresh(tarefa)
        return tarefa

    def atualizar(self, tarefa: Tarefas):
        self.db.commit()
        self.db.refresh(tarefa)
        return tarefa

    def deletar(self, tarefa: Tarefas):
        self.db.delete(tarefa)
        self.db.commit()
        return True