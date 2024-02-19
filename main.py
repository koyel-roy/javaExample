from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from database import connect, create_user, initialize_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    #LOAD the db
    initialize_db()
    print("lifespan start")
    yield
    print("lifespan end")

USE_LIFESPAN = False

app = FastAPI(lifespan=lifespan)


conn = connect()
cursor = conn.cursor()




@app.post("/users/")
async def add_user(name: str, age: int):
    user_id = create_user(name, age)
    if user_id:
        return {"id": user_id, "name": name, "age": age}
    else:
        raise HTTPException(status_code=400, detail="User not created")
    