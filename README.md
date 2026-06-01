## Gerenciador de Tarefas API

Projeto desenvolvido para aprendizado de desenvolvimento backend utilizando Python e FastAPI.

## Objetivo

Criar uma API de gerenciamento de tarefas e evoluí-la gradualmente com tecnologias utilizadas no mercado, documentando cada etapa do aprendizado e da implementação.

## Tecnologias Utilizadas

- Python 3
- FastAPI
- Pydantic
- Uvicorn

## Funcionalidades da Versão 1.0

- Criar tarefas
- Listar tarefas
- Buscar tarefa por ID
- Atualizar tarefas
- Excluir tarefas
- Validação de dados com Pydantic
- Tratamento de erros HTTP (404)
- Documentação automática com Swagger

## Estrutura Atual

```text
projeto-gerenciamento/
│
├── main.py
├── README.md
├── .gitignore
└── venv/
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
- [ ] Integração com MySQL
- [ ] SQLAlchemy

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
