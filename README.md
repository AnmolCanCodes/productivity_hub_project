# Personal Productivity Hub

Personal Productivity Hub is a backend API built with FastAPI, SQLAlchemy, and PostgreSQL to help users manage daily tasks, organize work into categories, and authenticate securely.

This project is designed to serve as a clean, modular foundation for a productivity application where users can register, log in, create tasks, and organize them using categories.

## Why this project exists

The goal of this project is to provide a reliable backend for a productivity application with:

- secure user authentication
- task management
- category-based organization
- a structured, maintainable codebase

## Features

- User registration and login
- JWT-based authentication
- Task creation and retrieval
- Category CRUD operations
- PostgreSQL database integration using SQLAlchemy ORM
- Clean layered architecture with routers, services, schemas, and models

## Tech Stack

- Python 3.12+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Passlib
- python-jose
- Uvicorn

## Project Structure

```text
app/
  auth/           # authentication helpers
  models/         # SQLAlchemy ORM models
  routers/        # FastAPI endpoints
  schemas/        # request/response validation models
  services/       # business logic
  config.py       # environment settings
  database.py     # database connection and session setup
  main.py         # FastAPI application entry point
```

## Prerequisites

Before running the project, make sure you have:

- Python 3.12 or newer installed
- PostgreSQL installed and running
- a database created named `productivity_hub`

## Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/AnmolCanCodes/productivity_hub_project
cd productivity_hub_project
```

2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create your environment file

```bash
cp .env.example .env
```


```

## Run the Application

Start the server with:

```bash
uvicorn app.main:app --reload
```

Once running, you can visit:

- API documentation: http://localhost:8000/docs
- Root endpoint: http://localhost:8000/

## API Examples

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

Create the database:

```sql
CREATE DATABASE productivity_hub;
```

Connect to the database:

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


