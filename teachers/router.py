from fastapi import APIRouter, Depends
from databases import get_db
from teachers.schema import TeacherCreate, TeacherResponse
from teachers.models import Teacher
from sqlalchemy.orm import Session

# Create a router instance
router3 = APIRouter(
    prefix="/teachers",
    tags=["teachers"],
    responses={404: {"description": "Not found"}},
)


@router3.get("/dashboard")
async def read_admin_dashboard():
    return {"username": "admin", "access": "full"}

@router3.post("/add_teacher")
def create_teacher(
    teacher: TeacherCreate,
    db: Session = Depends(get_db)
):
    new_teacher = Teacher (
        first_name = teacher.first_name,
        last_name = teacher.last_name,
        email= teacher.email,
        subject= teacher.subject,
        school_id= teacher.school_id
    )

    db.add(new_teacher)      # stage the object
    db.commit()              # save to DB
    db.refresh(new_teacher)  # get generated ID

    return new_teacher