from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import RegisterUser, LoginUser
from app.service.auth import AuthService

from fastapi.responses import HTMLResponse, JSONResponse
from app.core.database import get_db
from app.repository.user_repo import UserRepository



auth_router = APIRouter(prefix="/auth", tags=["authentication"])

async def get_auth_service(db: AsyncSession = Depends(get_db)):
    user_repo = UserRepository(db)
    return AuthService(user_repo)

@auth_router.post("/login")
async def login(login_date: LoginUser,
                auth_service: AuthService = Depends(get_auth_service)):
    result = await auth_service.authenticate_user(email = login_date.email, password = login_date.password)
    if not result:
        raise HTTPException(status_code=400, detail="Неверный email или пароль")
    print('trueeee123')
    return HTMLResponse(status_code=200)


@auth_router.post("/sign_up")
async def regist(register_date: RegisterUser,
                 auth_service: AuthService = Depends(get_auth_service)):
    # Проверяем есть ли такой user
    is_exist = await auth_service.check_email(email = register_date.email)
    if is_exist:
        print('12321321321323333333333333333333222222222255522')
        print('12321321321323333333333333333333222222222255522')
        print('12321321321323333333333333333333222222222255522')
        raise HTTPException(status_code=400, detail="Аккаунт с таким Email уже существует")
    # новый user
    print('1232132132132322222222')
    print('123213213213232222222222')

    result = await auth_service.new_user(name=register_date.name, email=register_date.email, password=register_date.password)
    # Возращаем ответ
    if result is not None:
    #     return JSONResponse(
    #         status_code=status.HTTP_201_CREATED,
    #         content={"message": "Аккаунт создан", "user_id": result.id}
    #     )
    # else:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="Произошла ошибка при создании аккаунта"
    #     )

    #     return HTMLResponse(status_code=200)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "Аккаунт создан", "user_id": result.id}
        )
    else:
        raise HTTPException(status_code=400, detail="Произошла ошибка" )


