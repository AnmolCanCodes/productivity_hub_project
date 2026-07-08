# Personal Productivity Hub

A FastAPI + SQLAlchemy + PostgreSQL backend for managing users, tasks, and categories.

## Features

- User registration and login
- JWT-based authentication
- Task creation and listing
- Category CRUD endpoints
- PostgreSQL persistence with SQLAlchemy ORM

## Tech Stack

- Python 3.12+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Passlib + python-jose

## Project Structure

```text
app/
  auth/
  models/
  routers/
  schemas/
  services/
  config.py
  database.py
  main.py
```

## Setup

1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create your environment file

```bash
cp .env.example .env
```

4. Update `.env` with your local PostgreSQL credentials and secret key.

## Run the API

```bash
uvicorn app.main:app --reload
```

Then open:

- API docs: http://localhost:8000/docs
- Root endpoint: http://localhost:8000/

## Example API Requests

### Register a user

```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"demo","email":"demo@example.com","password":"secret123"}'
```

### Login

```bash
curl -X POST "http://localhost:8000/auth/login" \
  -d "username=demo&password=secret123"
```

### Create a category

```bash
curl -X POST http://localhost:8000/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Work"}'
```

### List categories

```bash
curl http://localhost:8000/categories/
```

## PostgreSQL Commands

Create database:

```sql
CREATE DATABASE productivity_hub;
```

Connect:

```bash
psql -U postgres -d productivity_hub -h localhost
```

Useful queries:

```sql
\dt
SELECT * FROM users;
SELECT * FROM tasks;
SELECT * FROM categories;
```
