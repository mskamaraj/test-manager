from pydantic import BaseModel
from typing import Optional


class TestCaseCreate(BaseModel):
    name: str
    description: Optional[str] = None


class TestCase(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
