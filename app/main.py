from fastapi import FastAPI
from app.config import settings
from app.routers import auth, tasks
from app.database import engine, Base
from app.routers import categories


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(categories.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Personal Productivity Hub"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)