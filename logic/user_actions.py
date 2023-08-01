from typing import Tuple

from sqlalchemy.orm import Session

from db.crud_user import add_user_in_db, get_user_hashed_password_from_db
from logic.bcrypt_process import get_password_hash, verify_password
from logic.json_web_token import create_jwt_access_token


def add_user(user_name: str, password: str, db: Session) -> Tuple[int, str]:
    hashed_password = get_password_hash(password)
    status, user_id = add_user_in_db(user_name, hashed_password, db)
    if status == 1:
        generated_token = create_jwt_access_token(user_id, None)
        return 1, generated_token
    else:
        return 0, ""


def validate_user(username: str, password: str, db: Session):
    user_info = get_user_hashed_password_from_db(username, db)
    if user_info is None:
        return ""
    else:
        user_id, hashed_password = user_info
        if verify_password(password, hashed_password):
            generated_token = create_jwt_access_token(user_id, None)
            return generated_token
        return ""
