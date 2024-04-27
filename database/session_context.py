from loguru import logger
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from database.models.base import Base
from envfile import conf as config
import datetime
from contextlib import asynccontextmanager

engine = create_async_engine(url=config.db.PG_URI, echo=config.test)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)


@asynccontextmanager
async def get_async_session():
    session = sessionmaker()
    try:
        yield session
    except Exception as e:
        logger.error(e)
        await session.rollback()
    finally:
        await session.close()


def async_session_context(func):
    async def warper(*args, **kwargs):
        async with get_async_session() as session:
            async with session.begin():
                res = await func(session, *args, **kwargs)
                return res

    return warper
