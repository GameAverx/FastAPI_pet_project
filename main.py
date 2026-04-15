from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.models import user
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator
from app.core.database import init_bd, close_bd, engine
from app.api.v1.auth import auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await init_bd()
        yield
        await close_bd()

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)


@app.get("/", response_class=HTMLResponse)
async def get_index_page():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


# Base.metadata.create_all(bind=engine)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)

# taskkill /F /IM python.exe

# GameAverx
# user@example.com
# 555888123

# Alex
# user1235@example.com
# stringst