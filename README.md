# Expense Tracker API

REST API for managing personal expenses, with user authentication via JWT. Based on the [Expense Tracker API](https://roadmap.sh/projects/expense-tracker-api) project from roadmap.sh.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy (ORM)
- SQLite
- python-jose (JWT)
- passlib / bcrypt (password hashing)

## Project Structure

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

## Features

- User registration and login with JWT
- Expense CRUD protected by authentication
- Each user can only access their own expenses
- Ownership-based authorization: returns `403` when trying to update or delete another user's expense
- Expense categories via a fixed Enum: `Groceries`, `Leisure`, `Electronics`, `Utilities`, `Clothing`, `Health`, `Others`
- List filters:
  - by period: `week`, `month`, `3months`
  - by custom range: `start_date` / `end_date`

## Prerequisites

- Python 3.x

## Getting Started

1. Create and activate a virtual environment:

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

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with the `SECRET_KEY` variable:
   ```
   SECRET_KEY=your_secret_key_here
   ```

4. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

5. Open the interactive docs at http://127.0.0.1:8000/docs

The SQLite database (`expenses.db`) is created automatically on first run, since `main.py` calls `Base.metadata.create_all`.

## Environment Variables

| Variable     | Description                          |
|--------------|--------------------------------------|
| `SECRET_KEY` | Key used to sign JWT tokens          |

## Endpoints

| Method | Route                    | Description                              |
|--------|--------------------------|------------------------------------------|
| POST   | `/auth/register`         | Register a new user                      |
| POST   | `/auth/login`            | Authenticate the user and return a JWT   |
| POST   | `/expenses/create`       | Create an expense                        |
| GET    | `/expenses/list`         | List the user's expenses                 |
| PUT    | `/expenses/update/{id}`  | Update an expense                        |
| DELETE | `/expenses/delete/{id}`  | Delete an expense                        |

All `/expenses` routes require authentication (JWT token).

### Query params for `GET /expenses/list`

| Parameter    | Description                        |
|--------------|------------------------------------|
| `period`     | `week`, `month` or `3months`       |
| `start_date` | Start date (`YYYY-MM-DD`)          |
| `end_date`   | End date (`YYYY-MM-DD`)            |
