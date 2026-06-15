from pydantic import BaseModel
from typing import Optional


class TarefaBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    concluida: bool = False


class TarefaCreate(TarefaBase):
    pass


class TarefaResponse(TarefaBase):
    id: int

    class Config:
        from_attributes = True