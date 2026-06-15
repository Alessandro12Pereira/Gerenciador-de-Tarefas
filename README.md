## Gerenciador de Tarefas API

Projeto desenvolvido para aprendizado de desenvolvimento backend utilizando Python e FastAPI.

## Objetivo

Criar uma API de gerenciamento de tarefas e evoluí-la gradualmente com tecnologias utilizadas no mercado, documentando cada etapa do aprendizado e da implementação.

## Tecnologias Utilizadas
### Versão 1.0
* Python 3
* FastAPI
* Pydantic
* Uvicorn

### Versão 2.0
* MySQL
* SQLAlchemy
* PyMySQL

### Versão 3.0
* Python 3
* FastAPI
* Pydantic
* MySQL
* SQLAlchemy
* PyMySQL
* Uvicorn

## Funcionalidades da Versão 1.0
* Criar tarefas
* Listar tarefas
* Buscar tarefa por ID
* Atualizar tarefas
* Excluir tarefas
* Validação de dados com Pydantic
* Tratamento de erros HTTP (404)
* Documentação automática com Swagger

## Funcionalidades da Versão 2.0
* Integração com banco de dados MySQL
* Persistência de dados com SQLAlchemy ORM
* Criação automática de tabelas a partir dos models
* CRUD completo conectado ao banco de dados
* Gerenciamento de sessões com SQLAlchemy
* Consultas no banco (query, filter, first, all)
* Melhoria na estrutura do backend com separação entre model e conexão

## Funcionalidades da Versão 3.0
* Refatoração completa da arquitetura do projeto seguindo padrões de Clean Architecture e DDD
* Implementação do Repository Pattern para isolamento total da camada de acesso ao banco de dados
* Criação da Service Layer para centralização de regras de negócio e validações customizadas
* Aplicação prática de Injeção de Dependências nas rotas da API
* Desacoplamento de responsabilidades (Rotas apenas gerenciam requisições e respostas HTTP)
* Correção de concorrência e tipagem de dados nas operações do ORM

## Estrutura Atual
```text
projeto-gerenciamento/
│
├── app/
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py          # Conexão e sessão do banco de dados MySQL
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── tarefa.py            # Modelos ORM (SQLAlchemy)
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── tarefa_repository.py # Camada de persistência e consultas SQL
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── tarefa_routes.py     # Endpoints e controle de requisições HTTP
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── tarefa_schema.py     # Schemas de validação de dados (Pydantic)
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── tarefa_service.py    # Camada de regras de negócio e validações
│   │
│   └── main.py                  # Inicialização da API FastAPI e roteamento
│
├── .gitignore                   # Arquivos ignorados pelo Git
├── README.md                    # Documentação do projeto
├── requirements.txt             # Dependências do projeto
└── venv/                        # Ambiente virtual (não versionado)
```
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
- [x] Organização em camadas
- [x] Separação de rotas e serviços

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
