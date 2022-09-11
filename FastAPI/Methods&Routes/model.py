"""
    Our model to manage data
"""
from typing import Optional

from pydantic import BaseModel


class Person(BaseModel):
    """
        Person class
    """
    id: Optional[int] = None
    name: str
    age: int
    alive: Optional[bool] = None
    