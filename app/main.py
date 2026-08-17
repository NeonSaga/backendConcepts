from fastapi import FastAPI
from app.routes.todos import router
from app.database import Base, engine
from app.models.todo import Todo


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)










   