from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Tarefas(Base):
    __tablename__ = "tarefas"
    
    id = Column(Integer, primary_key = True, index = True)
    
    titulo = Column(String(255))
    
    descricao = Column(String(500))
    
    concluida = Column(Boolean, default = False)