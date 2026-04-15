from pydantic import BaseModel, Field, field_validator, EmailStr
from datetime import datetime


class RegisterUser(BaseModel):
    name: str = Field(..., max_length=40)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=50)

    @field_validator('name')
    def name_not_empty(cls, n: str) -> str:
        # убрать пробелы
        n = n.strip()
        # проверить что строка не пустая
        if not n:
            raise ValueError('Name cannot be empty')
        # вернуть значение
        return n

    @field_validator('password')
    def password_not_empty(cls, p: str) -> str:
        # убрать пробелы
        p = p.strip()
        # проверить что строка не пустая
        if not p:
            raise ValueError('Password cannot be empty')
        # вернуть значение
        return p

class LoginUser(BaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    def validate_password(cls, p: str) -> str:
        if not p or len(p) < 1:
            raise ValueError('Пароль не может быть пустым')
        return p




class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    created_at: datetime




