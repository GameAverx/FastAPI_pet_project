from sqlalchemy.orm import Session
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email==email)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
        # return self.db.query(User).filter(User.email == email).first()

    async def create_new_user(self, name: str, email: str, hashed_password: str) -> User:
        new_user = User(name=name,
                        email=email,
                        hashed_password=hashed_password)
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user

