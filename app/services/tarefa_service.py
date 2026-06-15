from app.repositories.tarefa_repository import TarefaRepository
from app.schemas.tarefa_schema import TarefaCreate
from app.models.tarefa import Tarefas

class TarefaService:

    def __init__(self, repository: TarefaRepository):
        self.repository = repository

    def listar_todas(self):
        return self.repository.listar()

    def buscar_por_id(self, tarefa_id: int):
        tarefa = self.repository.buscar_por_id(tarefa_id)
        if not tarefa:
            raise Exception("Tarefa não encontrada")
        return tarefa

    def criar(self, tarefa: TarefaCreate):
        
        if not tarefa.titulo or tarefa.titulo.strip() == "":
            raise ValueError("O título da tarefa é obrigatório")

        db_tarefa = Tarefas(
            titulo=tarefa.titulo,
            descricao=tarefa.descricao,
            concluida=tarefa.concluida
        )
        return self.repository.criar(db_tarefa)
    
    def atualizar(self, tarefa_id: int, tarefa_dados: TarefaCreate):
        db_tarefa = self.repository.buscar_por_id(tarefa_id)
        if not db_tarefa:
            return None
        
        
        db_tarefa.titulo = tarefa_dados.titulo
        db_tarefa.descricao = tarefa_dados.descricao
        db_tarefa.concluida = tarefa_dados.concluida
        
        return self.repository.atualizar(db_tarefa)
    
    def deletar(self, tarefa_id: int):
        db_tarefa = self.repository.buscar_por_id(tarefa_id)
        if not db_tarefa:
            return False
        
        return self.repository.deletar(db_tarefa)