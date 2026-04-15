from app.repository.user_repo import UserRepository
from app.core.security import hash_password, verify_password


class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo


    async def check_email(self, email: str):
        user = await self.user_repo.get_by_email(email)
        if user is None:
            return None
        return user

    async def authenticate_user(self, email: str, password: str):
        user = await self.check_email(email)
        if user is None:
            return None
        if not verify_password(password,user.hashed_password):
            return None
        return user

    async def new_user(self, name: str, email: str, password: str):
        new_user = await self.user_repo.create_new_user(name, email, hash_password(password))
        # return new_user

        if new_user.id:
            print(f"✅ Пользователь создан с id={new_user.id}")
            return new_user
        return None
