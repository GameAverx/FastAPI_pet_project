from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Создаем базовый класс для всех моделей
DATABASE_URL = "postgresql://user:pass@localhost/db"

# один поток ток
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db  #тПередаем db в роут
    finally:
        db.close()  # Закрываем соединение (даже если ошибка)







