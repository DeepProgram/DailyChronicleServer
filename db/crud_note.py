from typing import Tuple, List

from sqlalchemy.orm import Session

from db.db_models import NoteInfo


def add_note_in_db(note_title: str, note_body: str, added_time: int, user_id: str,
                   db: Session) -> bool:
    try:
        note_table_row = NoteInfo(user_id, note_title, note_body, added_time, added_time)
        db.add(note_table_row)
        db.commit()
        return True
    except Exception:
        return False


def get_notes_from_db(user_id: str, db: Session) -> Tuple[int, List]:
    try:
        notes_list = db.query(NoteInfo.index, NoteInfo.note_title, NoteInfo.note_body).order_by(
            NoteInfo.modification_time.desc()).filter(NoteInfo.user_id == user_id).all()
        modified_note_list = []
        for note in notes_list:
            temp_dict = {
                "note_title": note[1],
                "note_body": note[2],
                "selected": False,
                "note_id": note[0]
            }
            modified_note_list.append(temp_dict)
        return 1, modified_note_list
    except Exception:
        return 0, []


def update_notes_in_db(note_id: int, note_title: str, note_body: str, modification_time: int, user_id: str,
                       db: Session) -> int:
    try:
        db.query(NoteInfo). \
            filter(NoteInfo.index == note_id, NoteInfo.user_id == user_id). \
            update(
            {
                'note_title': note_title,
                "note_body": note_body,
                "modification_time": modification_time
            })
        db.commit()
        return 1
    except Exception:
        return 0


def delete_note_From_db(note_id: int, user_id: str, db: Session):
    try:
        db.query(NoteInfo).filter(NoteInfo.user_id == user_id, NoteInfo.index == note_id).delete()
        db.commit()
        return 1
    except Exception:
        return 0