# API de Chamados

**Aluno:** Wallace Gustavo Da Silva

API de Chamados desenvolvida em Python com FastAPI para a disciplina de Laboratório de Programação Full Stack.

Os dados são armazenados temporariamente em memória.

## Tecnologias

- Python
- FastAPI
- Uvicorn
- Pydantic

## Estrutura

api_chamados/
├── .venv/

├── main.py

├── capturas_tela/

├── requirements.txt

└── README.md

## Como executar

Criar o ambiente virtual:

    python -m venv .venv

Ativar no Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Instalar as dependências:

    pip install fastapi uvicorn

Executar a API:

    python -m uvicorn main:app --reload

Acessar a documentação:

    http://127.0.0.1:8000/docs

## Endpoints

| Método | Endpoint | Função |
|---|---|---|
| GET | / | Verifica se a API está funcionando |
| GET | /chamados | Lista os chamados |
| POST | /chamados | Cadastra um chamado |
| GET | /chamados/{chamado_id} | Busca chamado por ID |
| GET | /chamados/status/{status_chamado} | Filtra chamados por status |

## Exemplo de cadastro

    {
      "titulo": "Não consigo acessar o sistema",
      "descricao": "A tela de autenticação informa que minhas credenciais são inválidas.",
      "prioridade": "alta"
    }

O cadastro válido retorna `201 Created`.

O chamado recebe automaticamente o status `aberto`.

## Validação

Os campos obrigatórios são:

- `titulo`
- `descricao`
- `prioridade`

O envio de dados incompletos é rejeitado automaticamente pelo Pydantic.

## Testes

Foram realizados testes de:

- Cadastro de chamado.
- Listagem de chamados.
- Busca por ID.
- ID inexistente (`404`).
- Validação de campos obrigatórios (`422`).
- Filtro por status.

As evidências estão na pasta `capturas_tela/`.

## Dependências

Gerar o arquivo `requirements.txt`:

    pip freeze > requirements.txt

Instalar as dependências:

    pip install -r requirements.txt

## Observação

Os dados são armazenados apenas em memória. Ao reiniciar a aplicação, os chamados cadastrados são perdidos.
