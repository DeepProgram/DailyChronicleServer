from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db import db_models
from db.db_sql import engine
from routers import user, note

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.router)
app.include_router(note.router)
db_models.Base.metadata.create_all(bind=engine)
