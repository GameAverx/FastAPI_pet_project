from sqlalchemy.orm import Session
from app.models.user import User
from pydantic import EmailStr


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    async def get_by_email(self, email: str):
        try:
            return self.db.query(User).filter(User.email == email).first()
        except:
            return None
    async def create_new_user(self, name: str, email: EmailStr, hashed_password: str):
        new_user = User(name=name,
                        email=email,
                        hashed_password=hashed_password)
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user

