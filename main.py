from fastapi import FastAPI

from database import Base, engine
import models
from routers import auth_router, expenses_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")

app.include_router(auth_router.router)
app.include_router(expenses_router.router)