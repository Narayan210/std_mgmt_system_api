from fastapi import APIRouter, Depends
from students.schema import StudentCreate
from databases import get_db, engine, Base
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from students.models import Student

# Create a router instance
router2 = APIRouter(
    prefix="/students",
    tags=["students"],
    responses={404: {"description": "Not found"}},
)


@router2.get("/dashboard")
async def read_admin_dashboard():
    return {"username": "admin", "access": "full"}




@router2.post("/add_student")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    new_student = Student(
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email,
        grade=student.grade,
        enrollment_date=student.enrollment_date,
        school_id= student.school_id
    )

    db.add(new_student)      # stage the object
    db.commit()              # save to DB
    db.refresh(new_student)  # get generated ID

    return new_student
