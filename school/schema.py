   #school/schema.py
from pydantic import BaseModel
from datetime import datetime

class SchoolBase(BaseModel):
    name: str
    address: str | None = None
    phone: str | None = None
    email: str | None = None

class SchoolCreate(SchoolBase):
    pass

class SchoolResponse(SchoolBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
