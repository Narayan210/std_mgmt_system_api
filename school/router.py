
from fastapi import APIRouter, Depends, HTTPException
from school.schema import SchoolCreate, SchoolBase
from databases import get_db, engine, Base
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from school.models import School



# Create a router instance
router1 = APIRouter(
    prefix="/school",
    tags=["school"],
    responses={404: {"description": "Not found"}},
)


@router1.get("/dashboard")
async def read_admin_dashboard():
    return {"username": "admin", "access": "full"}


@router1.post("/add_school")
def create_student(
    school: SchoolCreate,
    db: Session = Depends(get_db)
):
    new_school = School(
        name=school.name,
        email=school.email,
        phone= school.phone,
        address=school.address
        
    )

    db.add(new_school)      # stage the object
    db.commit()              # save to DB
    db.refresh(new_school)  # get generated ID

    return new_school


@router1.delete("/delete_school/{school_id}")
def delete_school(
    school_id: int,
    db: Session= Depends(get_db)
):
    school= db.query(School).filter(School.id==school_id).first()
    

    if school is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(school)
    db.commit()

    return {"message": "Item deleted successfully"}
    
    