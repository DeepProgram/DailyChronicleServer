from pydantic import BaseModel, Field


class SignupInfo(BaseModel):
    username: str = Field(min_length=4)
    password: str = Field(min_length=8)


class NoteInfo(BaseModel):
    note_title: str
    note_body: str
