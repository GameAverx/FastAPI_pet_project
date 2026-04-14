from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator
from app.api.v1.auth import auth_router
from app.core.database import Base, engine


app = FastAPI()

app.include_router(auth_router, tags=["auth"])




@app.get("/", response_class=HTMLResponse)
async def get_index_page():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


@app.post("/login")
def login(email: str, password: str):
    # Проверяем есть ли такой user

    # Возращаем ответ

    return {"item_id": item_id, "q": q}

@app.post("/sign_up")
def sign_up(item_id: int, q: str | None = None):
    # Проверяем есть ли такой user

    # Возращаем ответ

    return {"item_id": item_id, "q": q}


def is_exist(email: str, password: str) :
    pass


Base.metadata.create_all(bind=engine)