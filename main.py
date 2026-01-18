from fastapi import FastAPI
import uvicorn
from school.router import router1
from students.router import router2
from teachers.router import router3
from databases import Base, engine



app= FastAPI()


# Create the tables (just in case you add models later)
Base.metadata.create_all(bind=engine)

@app.get("/")
def roots():
    return "welcome to the school management api"

app.include_router(router1)
app.include_router(router2)
app.include_router(router3)

if __name__=="__main__":
    uvicorn.run(app)