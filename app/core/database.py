from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# Создаем базовый класс для всех моделей
Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as session:
    # db = AsyncSessionLocal()
        try:
            yield session  #Передаем db в роут
        finally:
            session.close()  # Закрываем соединение (даже если ошибка)

async def init_bd():
    async with engine.begin() as conn:
        # run_sync позволяет выполнить синхронную операцию create_all
        await conn.run_sync(Base.metadata.create_all)

async def close_bd():
    await engine.dispose()





