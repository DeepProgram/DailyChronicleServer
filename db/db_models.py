from sqlalchemy import Column, String, Integer
from db.db_sql import Base


class UserInfo(Base):
    __tablename__ = "user_info"
    user_id = Column(String, primary_key=True)
    username = Column(String)
    hashed_password = Column(String)

    def __int__(self, user_id, username, hashed_password):
        self.user_id = user_id,
        self.username = username
        self.hashed_password = hashed_password


class NoteInfo(Base):
    __tablename__ = "note_info"
    index = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    note_title = Column(String)
    note_body = Column(String)
    creation_time = Column(Integer)
    modification_time = Column(Integer)

    def __init__(self, user_id, note_title, note_body, creation_time, modification_time):
        self.user_id = user_id
        self.note_title = note_title
        self.note_body = note_body
        self.creation_time = creation_time
        self.modification_time = modification_time
