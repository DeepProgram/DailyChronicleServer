from sqlalchemy.orm import Session
from db.db_models import UserInfo
from uuid import uuid4
from typing import Optional, List, Tuple


def add_user_in_db(username: str, hashed_password: str, db: Session) -> Tuple[int, str]:
    try:
        user_id = str(uuid4())
        user_table_row = UserInfo()
        user_table_row.user_id = user_id
        user_table_row.username = username
        user_table_row.hashed_password = hashed_password
        db.add(user_table_row)
        db.commit()
        return 1, user_id
    except Exception:
        return 0, ""



def get_user_hashed_password_from_db(username: str, db: Session) -> Optional[List]:
    user_info = db.query(UserInfo.user_id, UserInfo.hashed_password).filter(
        UserInfo.username == username).first()
    return user_info
