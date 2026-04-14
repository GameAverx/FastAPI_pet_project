from http.client import HTTPException

from fastapi import FastAPI, APIRouter
from app.schemas.user import RegisterUser, LoginUser
from app.service.auth import AuthService
from pydantic import BaseModel, Field, field_validator, EmailStr

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator



auth_router = APIRouter(prefix="/auth", tags=["authentication"])

@auth_router.post("/login")
def login(login_date: LoginUser):
    result = AuthService.authenticate_user(email = login_date.email, password = login_date.password)
    if not result:
        raise HTTPException(status_code=400, detail="Неверный email или пароль" )

    return result


@auth_router.post("/sign_up")
def regist(register_date: RegisterUser):
    # Проверяем есть ли такой user
    if AuthService.check_email(email = register_date.email):
        raise HTTPException(status_code=400, detail="Аккаунт с таким Email уже существует")
    # новый user
    result = AuthService.new_user(name=register_date.name, email=register_date.email, password=register_date.password)

    # Возращаем ответ
    return result
