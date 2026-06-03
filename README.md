## Gerenciador de Tarefas API

Projeto desenvolvido para aprendizado de desenvolvimento backend utilizando Python e FastAPI.

## Objetivo

Criar uma API de gerenciamento de tarefas e evoluí-la gradualmente com tecnologias utilizadas no mercado, documentando cada etapa do aprendizado e da implementação.

## Tecnologias Utilizadas
## Versão 1.0
- Python 3
- FastAPI
- Pydantic
- Uvicorn
## Versão 2.0
- MySQL
- SQLAlchemy
- PyMySQL 

## Funcionalidades da Versão 1.0

- Criar tarefas
- Listar tarefas
- Buscar tarefa por ID
- Atualizar tarefas
- Excluir tarefas
- Validação de dados com Pydantic
- Tratamento de erros HTTP (404)
- Documentação automática com Swagger

## Funcionalidades da Versão 2.0

Integração com banco de dados MySQL  
Persistência de dados com SQLAlchemy ORM  
Criação automática de tabelas a partir dos models  
CRUD completo conectado ao banco de dados  
Gerenciamento de sessões com SQLAlchemy  
Consultas no banco (query, filter, first, all)  
Melhoria na estrutura do backend com separação entre model e conexão 


## Estrutura Atual

```text
projeto-gerenciamento/
│
├── main.py              # API FastAPI (rotas e lógica principal)
├── database.py         # Conexão com o banco de dados MySQL
├── models.py           # Modelos ORM (SQLAlchemy)
├── README.md           # Documentação do projeto
├── requirements.txt    # Dependências do projeto
├── .gitignore          # Arquivos ignorados pelo Git
└── venv/               # Ambiente virtual (não versionado)

## Como Executar

### Ativar ambiente virtual

```bash
venv\Scripts\activate
```

### Iniciar servidor

```bash
uvicorn main:app --reload
```

### Acessar documentação

```text
http://127.0.0.1:8000/docs
```

## Exemplo de Criação de Tarefa

```json
{
  "titulo": "Estudar FastAPI",
  "descricao": "Aprender criação de APIs",
  "concluida": false
}
```

## Roadmap de Evolução

### Versão 1.0
- [x] CRUD básico
- [x] Pydantic
- [x] Tratamento de erros

### Versão 2.0
- [x] Integração com MySQL
- [x] SQLAlchemy

### Versão 3.0
- [ ] Organização em camadas
- [ ] Separação de rotas e serviços

### Versão 4.0
- [ ] Autenticação JWT
- [ ] Cadastro de usuários

### Versão 5.0
- [ ] Docker

### Versão 6.0
- [ ] Testes automatizados

### Versão 7.0
- [ ] Redis

### Versão 8.0
- [ ] Deploy em nuvem

### Versão 9.0
- [ ] CI/CD
