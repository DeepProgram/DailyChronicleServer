from sqlalchemy.orm import Session
from typing import List, Union, Tuple
from db.crud_note import add_note_in_db, get_notes_from_db, update_notes_in_db, delete_note_From_db
from logic.json_web_token import ALGORITHM, SECRET_KEY
from jose import jwt, JWTError


def is_token_valid(token: str) -> List[bool | str]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload["id"]
        return [True, user_id]
    except JWTError:
        return [False, ""]


def process_and_add_notes(note_title: str, note_body: str, added_time: int,
                          token: str, db: Session) -> int:
    valid_token, user_id = is_token_valid(token)
    if not valid_token:
        return -1
    if add_note_in_db(note_title, note_body, added_time, user_id, db):
        return 1
    else:
        return 0


def process_and_get_notes(token: str, db: Session) -> Tuple[int, List]:
    valid_token, user_id = is_token_valid(token)
    if not valid_token:
        return -1, []
    return get_notes_from_db(user_id, db)


def process_and_update_notes(note_id: int, note_title: str, note_body: str, modification_time: int,
                             token: str, db: Session) -> int:
    valid_token, user_id = is_token_valid(token)
    if not valid_token:
        return -1
    return update_notes_in_db(note_id, note_title, note_body, modification_time, user_id, db)


def process_and_delete_note(note_id: int, token: str, db: Session):
    valid_token, user_id = is_token_valid(token)
    if not valid_token:
        return -1
    return delete_note_From_db(note_id, user_id, db)
