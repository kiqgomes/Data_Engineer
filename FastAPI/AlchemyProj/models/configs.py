from typing import List

from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):

    API_V: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://kiq:12345@localhost:5432/biblioteca"
    DBBaseModel = declarative_base()

def square_range(stop,start = 0,step = 1):
    """_summary_

    Args:
        stop (_type_): _description_
        start (int, optional): _description_. Defaults to 0.
        step (int, optional): _description_. Defaults to 1.

    Returns:
        _type_: _description_
    """
  return [i ** 2 for i in range(start,stop,step)]