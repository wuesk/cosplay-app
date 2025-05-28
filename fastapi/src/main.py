from fastapi import FastAPI

from .person import router as person_router
from .core.models import Base
from .character import router as character_router
from .database import engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Person API", version="1.0.0")

app.include_router(person_router.router)
app.include_router(character_router.router)

@app.get("/")
def read_root():
    return {"message": "Person API is running!"}