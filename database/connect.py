import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from config import POSTGRES_URL,POSTGRES_URL_ASYNC
import logging
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

logger=logging.getLogger(__name__)


def create_session():
    try:
        async_engine=create_engine(POSTGRES_URL_ASYNC)
        async_session=sessionmaker(async_engine,expire_on_commit=False,class_=AsyncSession)

    except Exception as e:
        logger.exception("error creating async session")
        raise e

    try:
        engine=create_engine(POSTGRES_URL)
        ssn=sessionmaker(engine,expire_on_commit=False)
    except Exception as e:
        logger.exception("error creating sync session")
        raise e
    
    return ssn,async_session

