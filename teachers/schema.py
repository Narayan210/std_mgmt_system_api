  #teacher
from pydantic import BaseModel
from datetime import date

class TeacherBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    subject: str
    hire_date: date

class TeacherCreate(TeacherBase):
    school_id: int

class TeacherResponse(TeacherBase):
    id: int
    school_id: int

    class Config:
        from_attributes = True
