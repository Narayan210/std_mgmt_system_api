
##
from pydantic import BaseModel
from datetime import date

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    grade: str
    enrollment_date: date

class StudentCreate(StudentBase):
    school_id: int

class StudentResponse(StudentBase):
    id: int
    school_id: int

    class Config:
        from_attributes = True