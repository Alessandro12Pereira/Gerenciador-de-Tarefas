from fastapi import FastAPI
from app.database.database import Base, engine
from app.routes import tarefa_routes


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gerenciador de Tarefas Profissional",
    description="API refatorada na arquitetura V3.0",
    version="3.0.0"
)

@app.get("/")
def home():
    return {"mensagem": "API funcionando na nova arquitetura V3.0!"}


app.include_router(tarefa_routes.router)