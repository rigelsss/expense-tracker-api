# Expense Tracker API

API REST para gerenciamento de despesas pessoais, com autenticação de usuários via JWT. Projeto baseado no desafio [Expense Tracker API](https://roadmap.sh/projects/expense-tracker-api) do roadmap.sh.

## Tecnologias

- Python
- FastAPI
- SQLAlchemy (ORM)
- SQLite
- python-jose (JWT)
- passlib / bcrypt (hash de senha)

## Estrutura de arquivos

```
expense-tracker-api/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
└── routers/
    ├── auth_router.py
    └── expenses_router.py
```

## Funcionalidades

- Registro e login de usuário com JWT
- CRUD de despesas protegido por autenticação
- Cada usuário só acessa suas próprias despesas
- Autorização por dono do item: retorna `403` ao tentar alterar ou excluir despesa de outro usuário
- Categorias de despesa via Enum fixo: `Groceries`, `Leisure`, `Electronics`, `Utilities`, `Clothing`, `Health`, `Others`
- Filtros na listagem:
  - por período: `week`, `month`, `3months`
  - por intervalo customizado: `start_date` / `end_date`

## Pré-requisitos

- Python 3.x

## Como rodar

1. Crie e ative um ambiente virtual:

   **Windows**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **Linux/macOS**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` na raiz do projeto com a variável `SECRET_KEY`:
   ```
   SECRET_KEY=sua_chave_secreta_aqui
   ```

4. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

5. Acesse a documentação interativa em http://127.0.0.1:8000/docs

O banco SQLite (`expenses.db`) é criado automaticamente na primeira execução, pois o `main.py` chama `Base.metadata.create_all`.

## Variáveis de ambiente

| Variável     | Descrição                          |
|--------------|------------------------------------|
| `SECRET_KEY` | Chave usada para assinar os tokens JWT |

## Endpoints

| Método | Rota                     | Descrição                         |
|--------|--------------------------|-----------------------------------|
| POST   | `/auth/register`         | Registra um novo usuário          |
| POST   | `/auth/login`            | Autentica o usuário e retorna o token JWT |
| POST   | `/expenses/create`       | Cria uma despesa                  |
| GET    | `/expenses/list`         | Lista as despesas do usuário      |
| PUT    | `/expenses/update/{id}`  | Atualiza uma despesa              |
| DELETE | `/expenses/delete/{id}`  | Exclui uma despesa                |

As rotas de `/expenses` exigem autenticação (token JWT).

### Query params de `GET /expenses/list`

| Parâmetro    | Descrição                                      |
|--------------|------------------------------------------------|
| `period`     | `week`, `month` ou `3months`                   |
| `start_date` | Data inicial (`YYYY-MM-DD`)                    |
| `end_date`   | Data final (`YYYY-MM-DD`)                      |
